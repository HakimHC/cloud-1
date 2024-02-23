from jinja2 import Template
import logging


class InventoryHandler:
    def __init__(self, config: dict):
        self.template_path = config.get('template_path')
        self.inventory_path = config.get('inventory_path')
        self.hosts = config.get('hosts')

    def build_inventory(self, hosts: list[dict]):
        logging.debug(f'Starting templating file: {self.template_path}')

        loaded_template_file = self.__load_template_file()
        template = Template(loaded_template_file)

        if self.hosts:
            hosts += self.hosts

        built_inventory = template.render(hosts=hosts)
        self.__save_inventory(built_inventory)

    def __load_template_file(self):
        try:
            with open(self.template_path, 'r') as f:
                return f.read()
        except (FileNotFoundError, PermissionError) as e:
            logging.error(e)

    def __save_inventory(self, new_content):
        try:
            with open(self.inventory_path, 'w') as f:
                f.write(new_content)
        except (FileNotFoundError, PermissionError) as e:
            logging.error(e)
            exit(1)
