# Import Standard Modules
import os
import sys
import pandas as pd

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0])


def read_data(data_path: str,
              data_separator: str,
              data_encoding: str) -> pd.DataFrame:
    """
    Read data from 'data_path' location
    :param data_path: String data location
    :param data_separator: String data CSV separator
    :param data_encoding: String data CSV file encoding
    :return: Pandas DataFrame of read data
    """

    logger.info('read_data - Start')

    try:

        logger.info('read_data - Read data from {}'.format(data_path))

        # Read data from CSV
        data = pd.read_csv(data_path,
                           sep=data_separator,
                           encoding=data_encoding)

    except Exception as e:

        logger.error('read_data - Unable to read data from {}'.format(data_path))
        logger.error(e)
        sys.exit(1)

    else:

        logger.info('read_data - Data read successfully')

    finally:

        logger.info('read_data - End')

    return data


