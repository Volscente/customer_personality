# Import Standard Modules
import os
import yaml

# Set root path
os.chdir(os.environ['CUSTOMER_PERSONALITY_PATH'])

def read_configuration(file_name):
    """

    :param file_name:
    :return:
    """

    try:
        
        # Read configuration file
        with open('../../configuration/' + file_name) as config_file:

            configuration = yaml.safe_load(config_file)

    except Exception as e:

        pass
    
    return configuration


