"""
Module defines the configuration reader for the application.
"""

import yaml
import logging


class Config:
    def __init__(self, config_file):
        self.config = self.read_config(config_file)

    def read_config(self, config_file):
        """
        Read the configuration file and return the configuration.
        """
        try:
            with open(config_file) as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
            return config
        except FileNotFoundError:
            logging.error("Configuration file not found")
            raise
