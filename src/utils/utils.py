# Import Standard Modules
import os
import yaml
import sys

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.logging_module.logging_module import get_logger

# Setup logger
logger = get_logger(os.path.basename(__file__).split('.')[0])


def read_configuration(file_name: str) -> dict:
    """

    :param file_name:
    :return:
    """

    logger.info('read_configuration - Start')

    try:

        logger.info('read_configuration - Reading {}'.format(file_name))
        
        # Read configuration file
        with open('./configuration/' + file_name) as config_file:

            configuration = yaml.safe_load(config_file)

    except Exception as e:

        logger.error('read_configuration - Unable to read {}'.format(file_name))
        logger.error(e)
        sys.exit(1)

    logger.info('read_configuration - End')

    return configuration


