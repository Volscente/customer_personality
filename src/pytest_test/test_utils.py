# Import Standard Modules
import os
import pytest

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.pytest_test.test_utils_fixtures import test_data_preparation
from src.utils.utils import read_configuration
from src.data_preparation.data_preparation import DataPreparation


def test_environment_variable(test_data_preparation: DataPreparation) -> bool:
    """
    Test the correct set of the env variables CUSTOMER_PERSONALITY_PATH
    :return: Boolean
    """

    assert os.getcwd() == os.environ['CUSTOMER_PERSONALITY_PATH']


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('config.yaml', 'data_path', './data/marketing_campaign.csv')
])
def test_read_configuration(test_config_file, ):
    """
    Test the function src.utils.utils.read_configuration
    :return: Boolean
    """

    # Read configuration file
    config = read_configuration()


