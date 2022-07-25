# Import Standard Modules
import pytest
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.data_preparation.data_preparation import DataPreparation


@pytest.fixture
def test_data_preparation() -> DataPreparation:
    """
    Fixture for an instance of the class DataPreparation
    :return: DataPreparation instance
    """

    return DataPreparation()
