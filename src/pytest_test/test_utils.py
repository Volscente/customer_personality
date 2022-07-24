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


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('config.yaml', 'data_path', './data/marketing_campaign.csv')
])
def test_read_configuration():
    """
    Test the function src.utils.utils.read_configuration
    :return:
    """


