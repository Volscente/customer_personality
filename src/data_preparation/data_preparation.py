# Import Standard Modules
import os
import pandas as pd
import numpy as np

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.utils.utils import read_configuration


class DataPreparation:

    def __init__(self):
        """
        Initialize a DataPreparation object for preparing and cleaning the data to the modeling phase
        """

        # Read Configuration file
        self.config = read_configuration('config.yaml')

        # Init instance variables
        self.data = None

    def run(self):
        """
        Run a pipeline for preparing and cleaning the data
        :return: Write prepared data as a .CSV file
        """

        # Read data
        pass