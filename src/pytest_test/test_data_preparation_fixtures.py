# Import Standard Modules
import pytest
import os
import pandas as pd

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.utils.utils import read_configuration


@pytest.fixture
def test_configuration() -> dict:
    """
    Test configuration object dictionary
    :return: Dictionary configuration
    """

    # Read configuration dictionary
    configuration = read_configuration('config.yaml')

    return configuration


@pytest.fixture
def test_data(test_configuration) -> pd.DataFrame:
    pass

