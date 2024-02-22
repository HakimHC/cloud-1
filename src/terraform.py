import os
import subprocess
import sys

from constants import PROJECT_ROOT
from pathlib import Path
import logging
from executor import CommandExecutor
import re


class TerraformHandler:
    def __init__(self, config: dict):
        self.base_dir = config.get('base_dir')
        self.terraform_dir = PROJECT_ROOT / self.base_dir
        self.apply = config.get('apply')

        self.__commands = ['terraform init']

        if self.apply:
            self.__commands += ['terraform apply -auto-approve']
            self.run_apply()

        self.get_output_info()

    def run_apply(self):
        CommandExecutor.execute_commands(
            commands=self.__commands,
            working_directory=self.terraform_dir
        )

    def get_output_info(self) -> dict:
        output = CommandExecutor.execute_commands(
            commands=['terraform output'],
            working_directory=self.terraform_dir
        )[0]

        parsed_output = []
        for line in output.split('\n'):
            if line:
                parsed_output.append(re.findall(r'(ip_address|user).*=.*\"(.*)\"', line)[0])

        result = {}
        for var in parsed_output:
            result[var[0]] = var[1]

        return result

