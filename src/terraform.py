from constants import PROJECT_ROOT
import logging
from executor import CommandExecutor
import re


class TerraformHandler:
    def __init__(self, config: dict):
        self.base_dir = config.get('base_dir')
        self.terraform_dir = PROJECT_ROOT / self.base_dir
        self.apply = config.get('apply')
        self.initialized = False

        self.__commands = ['terraform init']

        if self.apply:
            logging.info('Applying Terraform')
            self.initialized = True
            self.__commands += ['terraform apply -auto-approve']
            self.run_apply()

    def run_apply(self):
        CommandExecutor.execute_commands(
            commands=self.__commands,
            working_directory=self.terraform_dir,
            capture=False
        )

    def get_output_info(self) -> list[dict]:
        logging.info('Getting terraform output information')

        if not self.initialized:
            CommandExecutor.execute_commands(
                commands=['terraform init'],
                working_directory=self.terraform_dir,
                capture=True
            )

        output = CommandExecutor.execute_commands(
            commands=['terraform output'],
            working_directory=self.terraform_dir,
            capture=True
        )[0]

        try:
            parsed_output = []
            for line in output.split('\n'):
                if line:
                    parsed_output.append(re.findall(r'(ip_address|user).*=.*\"(.*)\"', line)[0])

            result = {}
            for var in parsed_output:
                result[var[0]] = var[1]
        except (IndexError, ValueError):
            logging.warning('No output found in terraform output, returning empty list')
            return []

        logging.info(f'Host information captured: {result}')
        return [result]

