# Import Standard Modules
import os
import pandas as pd
import numpy as np

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.utils.utils import read_configuration
from src.logging_module.logging_module import get_logger
from src.data_preparation.dp_utils import read_data, remove_useless_columns


class DataPreparation:

    def __init__(self, configuration_file='config.yaml'):
        """
        Initialize a DataPreparation object for preparing and cleaning the data to the modeling phase
        """

        # Setup Logger
        self.logger = get_logger(__class__.__name__)
        self.logger.info('__init__ - Instancing the class')

        self.logger.info('__init__ - Read configuration file')

        # Read Configuration file
        self.config = read_configuration(configuration_file)

        # Init instance variables
        self.data = None

    def run(self):
        """
        Run a pipeline for preparing and cleaning the data
        :return: Write prepared data as a .CSV file
        """

        self.logger.info('run - Running the pipeline')

        # Read data
        self.data = read_data(self.config['data_path'],
                              self.config['data_separator'],
                              self.config['data_encoding'])

        # Remove useless columns
        self.data = remove_useless_columns(self.data, self.config['useless_columns'])

