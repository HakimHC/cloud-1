from config import Config
from terraform import TerraformHandler
from ansible import AnsibleHandler
from inventory import InventoryHandler

import logging
import time


class Deployer:
    def __init__(self, config: Config):
        self.terraform = TerraformHandler(config.terraform)
        self.inventory = InventoryHandler(config.inventory)
        self.ansible = AnsibleHandler(config.ansible)

    def deploy(self):
        hosts = []
        hosts = self.terraform.get_output_info()

        self.inventory.build_inventory(
            hosts=hosts
        )
        # TODO: obviously change it to a ping or something like that
        logging.info('Waiting for Terraform hosts')
        time.sleep(2)
        self.ansible.run_playbook(
            inventory_path=self.inventory.inventory_path
        )

