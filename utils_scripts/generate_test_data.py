# Import Standard Modules
import pandas as pd
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.utils.utils import read_configuration
from src.data_preparation.dp_utils import read_data, remove_useless_columns


def generate_test_data(sample_size=10):

    pass


def main():

    generate_test_data(20)


main()
