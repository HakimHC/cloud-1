from constants import PROJECT_ROOT
from pathlib import Path
import logging


class TerraformHandler:
    def __init__(self, config: dict):
        self.base_dir = config.get('base_dir')
        self.terraform_dir = PROJECT_ROOT / self.base_dir
        self.apply = config.get('apply')

        self.__commands = ['terraform init']

        if self.apply:
            self.__commands += ['terraform apply -auto-approve']

        self.__execute_commands(self.__commands)

    def apply(self):
        pass

    def __execute_commands(self, commands: list[str]):
        logging.debug(f'Executing commands: {commands}')
