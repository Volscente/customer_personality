# Import Standard Modules
import pytest
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.data_preparation.dp_utils import read_data
from src.pytest_test.test_data_preparation_fixtures import test_configuration


@pytest.mark.parametrize('test_id, expected_year_birth, expected_education', [
    (5524, 1957, 'Graduation'),
    (2174, 1954, 'Graduation'),
    (5324, 1981, 'PhD')
])
def test_read_data(test_configuration: dict,
                   test_id: int,
                   expected_year_birth: int,
                   expected_education: str):
    """
    Test the function src.data_preparation.dp_utils.read_data
    :param test_configuration: Dictionary configuration object
    :param test_id: Integer id of the record to test
    :param expected_year_birth: Integer year_birth of the record to test
    :param expected_education: String education of the record to test
    """

    # Read data
    data = read_data(test_configuration['data_path'],
                     test_configuration['data_separator'],
                     test_configuration['data_encoding'])

    # Select record
    record = data[data['ID'] == test_id][['Year_Birth', 'Education']]

    assert record['Year_Birth'].iloc[0] == expected_year_birth and record['Education'].iloc[0] == expected_education


def test_read_data_exceptions():
    pass
