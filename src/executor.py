import logging
import os
import sys
import subprocess

from constants import PROJECT_ROOT


class CommandExecutor:
    @staticmethod
    def execute_commands(commands: list[str], working_directory=None, capture=False):
        output = []
        logging.debug(f'Executing commands: {commands}')

        if working_directory:
            os.chdir(working_directory)

        for command in commands:
            if capture:
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True
                )
            else:
                result = subprocess.run(
                    command,
                    shell=True,
                    stdout=sys.stdout,
                    stderr=sys.stderr
                )

            output.append(result.stdout)
            if result.returncode != 0:
                logging.error(result.stderr)
                exit(1)

        os.chdir(PROJECT_ROOT)
        return output

