# Import Standard Modules
import os
import pytest

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.pytest_test.test_utils_fixtures import test_data_preparation
from src.utils.utils import read_configuration
from src.data_preparation.data_preparation import DataPreparation


def test_environment_variable(test_data_preparation: DataPreparation):
    """
    Test the correct set of the env variables CUSTOMER_PERSONALITY_PATH
    :param test_data_preparation:
    """

    assert os.getcwd() == os.environ['CUSTOMER_PERSONALITY_PATH']


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('config.yaml', 'data_path', './data/marketing_campaign.csv')
])
def test_read_configuration(test_config_file: str,
                            test_config: str,
                            expected_value: str):
    """
    Test the function src.utils.utils.read_configuration
    :param test_config_file: String configuration file name
    :param test_config: String configuration entry key
    :param expected_value: String configuration expected value
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    ('wrong_config.config', FileNotFoundError)
])
def test_read_configuration_exception(test_config_file: str,
                                      expected_error: FileNotFoundError):

    with pytest.raises(expected_error):

        read_configuration(test_config_file)
