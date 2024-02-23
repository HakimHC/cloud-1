from executor import CommandExecutor
import logging


class AnsibleHandler:
    def __init__(self, config: dict):
        self.playbook_path = config.get('playbook_path')
        self.extra_vars = config.get('extra_vars')

        logging.info('Ansible handler initialized.')

    def run_playbook(self, inventory_path):
        command = f'ansible-playbook -i {inventory_path} {self.playbook_path} '
        if self.extra_vars:
            command += f'-e {self.__convert_extra_vars()}'
        CommandExecutor.execute_commands(
            [command],
            capture=False
        )

    def __convert_extra_vars(self) -> str:
        if not self.extra_vars:
            return ""
        vars_list = []

        for key, value in self.extra_vars.items():
            vars_list.append(f'{key}={value}')

        return " ".join(vars_list)
