# Import Standard Modules
import os

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

# Import Package Modules
from src.utils.utils import read_configuration
from src.data_preparation.dp_utils import read_data, remove_useless_columns


def generate_test_data(config_file: str,
                       test_data_file: str,
                       sample_size: int = 10) -> None:

    # Read configuration
    config = read_configuration(config_file)

    # Read data
    data = read_data(config['data_path'],
                     config['data_separator'],
                     config['data_encoding'])

    # Sample data
    data_sample = data.sample(sample_size)

    # Write to CSV file
    data_sample.to_csv(config['data_folder'] + test_data_file,
                       sep='\t',
                       encoding=config['data_encoding'],
                       index=False)


def main():

    generate_test_data(config_file='config.yaml',
                       test_data_file='marketing_campaign_test_data.csv',
                       sample_size=20)


main()
