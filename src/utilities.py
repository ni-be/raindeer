"""
Contains utility functions used for various functionalities.
"""
import os
import yaml
import pandas as pd


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(ROOT_DIR)

def load_dataset(dataset: str) -> pd.core.frame.DataFrame:
    """Loads the dataset and returns it as a dataframe.

    :param dataset: File path to the dataset in .csv format. Defaults to
    '../data/24311-0002_$F.csv'.
    :type dataset: str
    :return: Dataframe containing the data from the given dataset.
    :rtype: pandas.core.frame.DataFrame
    """
    
    data = pd.read_csv(dataset, sep=";", header=1, index_col=0)
    print(data)
    return data


def yaml_reader(option):
    """
    Yaml Reader allows reading the config.yaml in the root directory containing
    data points needed for running the application.
    :param option: choose which data point in config.yaml is needed
    :type option: string
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
    Functionality to save plots inside the results folder.

    :param plt: the finished plot
    :type plt: 'module'
    :param sub_dir: subdirectory for storage
    :type sub_dir: string
    :param filename: filename
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
        plt.savefig(f"{PARENT_DIR}/results/{sub_dir}/plots/{filename}.png")
        print(f"Successfully saved: /results/{sub_dir}/plots/{filename}.png")
 
    except Exception as e:
        print(f"An error occurred: {e}")
