# Import Standard Modules
import pytest
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])


@pytest.fixture
def test_configuration() -> dict:
    """
    Test configuration object dictionary
    :return: Dictionary configuration
    """

