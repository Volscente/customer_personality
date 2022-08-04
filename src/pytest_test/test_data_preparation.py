# Import Standard Modules
import sys

import pandas as pd
import pytest
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

from src.data_preparation.dp_utils import read_data, remove_useless_columns
from src.pytest_test.test_data_preparation_fixtures import test_configuration, test_data


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


@pytest.mark.parametrize('test_data_path, test_data_separator, expected_error', [
    ('./data/wrong_marketing_campaign.csv', '\t', FileNotFoundError)
])
def test_read_data_exception(test_data_path: str,
                             test_data_separator: str,
                             expected_error: FileNotFoundError):
    """
    Test exception triggers for the function src.data_preparation.dp_utils.read_data
    :param test_data_path: String test data path
    :param test_data_separator: String separator character
    :param expected_error: FileNotFoundError exception
    """

    with pytest.raises(expected_error):

        read_data(test_data_path, test_data_separator, 'latin1')


def test_remove_useless_columns(test_data: pd.DataFrame,
                                test_configuration: dict):
    """
    Test the function src.data_preparation.dp_utils.remove_useless_columns
    :param test_data: Pandas DataFrame of test data
    :param test_configuration: Dictionary configuration object
    """

    # Remove useless columns
    test_data_cleaned = remove_useless_columns(test_data,
                                               test_configuration['useless_columns'])

    # Retrieve the DataFrame columns
    test_data_columns = test_data_cleaned.columns

    # Initialize a bool for checking if the columns have been correctly dropped
    removed = True

    # Loop over the columns to remove
    for useless_column in test_configuration['useless_columns']:

        if useless_column in test_data_columns:

            removed = False

    assert removed


def test_remove_useless_columns_exceptions()



