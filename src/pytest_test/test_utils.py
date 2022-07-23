# Import Standard Modules
import os
import pytest

from src.pytest_test.test_utils_fixtures import test_data_preparation


def test_environment_variable(test_data_preparation):
    """
    Test the correct set of the env variables CUSTOMER_PERSONALITY_PATH
    :return:
    """

    assert os.getcwd() == os.environ['CUSTOMER_PERSONALITY_PATH']


def test_read_configuration(test_data_preparation):

    print(test_data_preparation.config)

