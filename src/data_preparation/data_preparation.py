# Import Standard Modules
import os
import pandas as pd
import numpy as np

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.utils.utils import read_configuration
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0])


class DataPreparation:

    def __init__(self, configuration_file='config.yaml'):
        """
        Initialize a DataPreparation object for preparing and cleaning the data to the modeling phase
        """

        logger.info('__init__ - Read configuration file')

        # Read Configuration file
        self.config = read_configuration(configuration_file)

        # Init instance variables
        self.data = None

    def run(self):
        """
        Run a pipeline for preparing and cleaning the data
        :return: Write prepared data as a .CSV file
        """

        logger.info('run - Running the pipeline')

        # Read data
        pass
