"""
Contains utility functions used for various functionalities.
"""
import os
import logging
import yaml
import pandas as pd


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(ROOT_DIR)


def load_dataset(dataset: str) -> pd.core.frame.DataFrame:
    """Load the specified dataset into a pandas dataframe.

    Args:
        dataset (str): Full path to the dataset in .csv format.
                       Defaults to '../data/24311-0002_$F.csv'.
    Returns:
        pd.core.frame.DataFrame: Dataframe containing the dataset.
    """

    data = pd.read_csv(dataset, sep=";", header=1, index_col=0)
    logging.info('Loading the data')
    print(data)
    return data


def yaml_reader(option):
    """
    Read the specified data point from the config.yaml file in root directory.

    Args:
        option (str): Data point in config.yaml that is to be read.

    Raises:
        ValueError: If the option is not found in the YAML file.

    Returns:
        Various: Returns the specific configuration data defined by option.
    """

    with open(f"{PARENT_DIR}/config.yaml", 'r') as file:
        data = yaml.safe_load(file)

    if option in data:
        return data[option]
    elif option == "root_data":
        data_dir = f"{PARENT_DIR}/data"
        return data_dir
    else:
        raise ValueError(f"Option {option} is not found in the YAML file.")


def plot_save(plt, sub_dir, filename):
    """
    Save the provided plot to the specified directory.

    Args:
        plt (matplotlib.pyplot): The configured matplotlib plot to be saved.
        sub_dir (str): Subdir under '/results' where the plot will be saved.
        filename (str): The filename to save the plot under.

    """

    assert isinstance(PARENT_DIR, str), "PARENT_DIR must be a string"
    assert isinstance(sub_dir, str), "sub_dir must be a string"
    assert isinstance(filename, str), "name must be a string"
    directory = f"{PARENT_DIR}/results/{sub_dir}/plots/"
    # Check if the directory exists
    if not os.path.exists(directory):
        # If the directory does not exist, create it
        os.makedirs(directory)
    try:
        logging.info('Saving the provided plot to the specified directory.')
        plt.savefig(f"{PARENT_DIR}/results/{sub_dir}/plots/{filename}.png")
        logging.info("Successfully saved.")
        print(f"Successfully saved: /results/{sub_dir}/plots/{filename}.png")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise e