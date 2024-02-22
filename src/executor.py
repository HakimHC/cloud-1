import logging
import os
import sys
import subprocess

from constants import PROJECT_ROOT


class CommandExecutor:
    @staticmethod
    def execute_commands(commands: list[str], working_directory=None):
        output = []
        logging.debug(f'Executing commands: {commands}')

        if working_directory:
            os.chdir(working_directory)

        for command in commands:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            print(result.stdout)
            output.append(result.stdout)
            if result.returncode != 0:
                print(result.stderr, file=sys.stderr)
                exit(1)

        os.chdir(PROJECT_ROOT)
        return output

