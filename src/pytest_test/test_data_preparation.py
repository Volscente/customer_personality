# Import Standard Modules
import pytest
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.data_preparation.dp_utils import read_data
from src.pytest_test.test_data_preparation_fixtures import test_configuration


def test_read_data(test_configuration: dict):

    data = read_data(test_configuration['data_path'],
                     test_configuration['data_separator'],
                     test_configuration['data_encoding'])
