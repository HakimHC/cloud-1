import logging
import os
import sys
import subprocess

from constants import PROJECT_ROOT


class CommandExecutor:
    @staticmethod
    def execute_commands(commands: list[str], working_directory=None, capture=False, retries=1):
        logging.debug(f'Executing commands: {commands}')

        if working_directory:
            os.chdir(working_directory)

        i = 0
        ret = {}
        while i < retries:
            ret = CommandExecutor.__exec(commands, capture)
            if ret.get('exit_code') == 0:
                break
            i += 1

        if i == retries:
            logging.error(f'Command execution failed. ({commands})')
            exit(1)
        os.chdir(PROJECT_ROOT)
        return [ret.get('stdout')]

    @staticmethod
    def __exec(
            commands: list[str],
            capture: bool
    ):
        ret = {}
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
            ret["stdout"] = result.stdout
            ret["stderr"] = result.stderr
            ret["exit_code"] = result.returncode

            if result.returncode != 0:
                return ret
        return ret
