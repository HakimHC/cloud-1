import json
import logging
import logging.config


class Logger:
    def __init__(self, config):
        self.config = config
        self.setup_logging()

    def setup_logging(self):
        logging_config = self.config.get('logging', {})
        log_file = logging_config.get('log_file', 'deployment.log')
        log_level = logging_config.get('level', 'INFO').upper()
        log_format = logging_config.get('format', '[%(asctime)s] - %(levelname)s - %(message)s')

        logging.basicConfig(filename=log_file, level=log_level, format=log_format, filemode='a')

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)
        logging.getLogger('').addHandler(console_handler)

