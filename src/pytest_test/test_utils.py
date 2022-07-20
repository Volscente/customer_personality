# Import Standard Modules
import os
import pytest

from src.pytest_test.test_utils_fixtures import test_data_preparation


def test_environment_variable(test_data_preparation):
    """

    :return:
    """
    print('Current Dir')
    print(os.getcwd())

    assert True

