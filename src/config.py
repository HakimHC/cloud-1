import json
from json.decoder import JSONDecodeError
import sys


class Config:
    class InvalidBlockError(Exception):
        def __init__(self, msg):
            super().__init__(msg)

    def __init__(self, file_path="config.json"):
        self.file_path = file_path
        self.raw_data = self.__read_config()
        self.config = self.__load_json()
        self.inventory = self.config.get('inventory')
        self.ansible = self.config.get('ansible')
        self.terraform = self.config.get('terraform')

        self.__validate_terraform_block()

    def __read_config(self):
        try:
            with open(self.file_path, 'r') as f:
                return f.read()
        except (FileNotFoundError, PermissionError) as e:
            print(f'Invalid configuration file: {e}', file=sys.stderr)
            exit(1)

    def __load_json(self):
        try:
            return json.loads(self.raw_data)
        except JSONDecodeError as e:
            print(f'Invalid configuration file: {e}', file=sys.stderr)
            exit(1)

    def __validate_terraform_block(self):
        Config.__validate_config_block(
            self.terraform,
            context='terraform',
            required_fields=['base_dir', 'run_apply', 'replace_inventory'],
            optional_fields=[]
        )

    def __validate_ansible_block(self):
        Config.__validate_config_block(
            self.ansible,
            context='ansible',
            required_fields=['playbook_path'],
            optional_fields=['extra_vars']
        )

    @staticmethod
    def __validate_config_block(
            obj: dict,
            context: str,
            required_fields: list[str],
            optional_fields: list[str]
    ):
        if not isinstance(obj, dict):
            raise Config.InvalidBlockError(f'Invalid {context} block (must be a dictionary).')

        all_fields = set(required_fields + optional_fields)
        config_fields = set(obj.keys())
        unknown_fields = config_fields - all_fields

        if unknown_fields:
            raise Config.InvalidBlockError(f'Unknown fields provided in {context} block: {unknown_fields}')

        missing_required_fields = set(required_fields) - config_fields
        if missing_required_fields:
            raise ValueError(f"Missing required fields in {context} block: {missing_required_fields}")

