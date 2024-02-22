import os
import subprocess
import sys

from constants import PROJECT_ROOT
from pathlib import Path
import logging
from executor import CommandExecutor


class TerraformHandler:
    def __init__(self, config: dict):
        self.base_dir = config.get('base_dir')
        self.terraform_dir = PROJECT_ROOT / self.base_dir
        self.apply = config.get('apply')

        self.__commands = ['terraform init']

        if self.apply:
            self.__commands += ['terraform apply -auto-approve']
            self.run_apply()

        CommandExecutor.execute_commands(
            commands=['terraform output'],
            working_directory=self.terraform_dir
        )

    def run_apply(self):
        CommandExecutor.execute_commands(
            commands=self.__commands,
            working_directory=self.terraform_dir
        )

