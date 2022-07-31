# customer_personality
Dataset regarding customer personalities and shopping habits

# Notebooks

## data_preparations
The notebook is intended to perform data cleaning process over the dataset marketing_campaign.csv.

## exploratory_data_analysis
The notebook is intended to perform an Exploratory Data Analysis (EDA) over the dataset marketing_campaign.csv.

## response_classification
The notebook is intended to perform a binary classification over the 'Response' label.

# Installation

## Python Requirements
The project uses [pipenv](https://realpython.com/pipenv-guide/) for managing python libraries and dependencies.
All the required python libraries can be found in the Pipfile.
To install the specified libraries, use the command

``` bash
pipenv install --ignore-pipfile
```

## Set Environment Variable
An environment variable pointing to the root path of the project directory is required
to ensure the interoperability among different OS.

Set the environment variable **"CUSTOMER_PERSONALITY_PATH"** to the root directory of this repository.

``` bash
export CUSTOMER_PERSONALITY_PATH="<absolute_path_to_root_directory"
```
