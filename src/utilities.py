"""
Contains utility functions used for various functionalities.
"""
import os
import yaml
import pandas as pd


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
    root_dir = os.path.dirname(os.path.abspath(__file__)) 
    parent_dir = os.path.dirname(root_dir)

    with open(f"{parent_dir}/config.yaml" , 'r') as file:
        data = yaml.safe_load(file)
        
    if option in data:
        return data[option]
    elif option == "root_data":
        data_dir = f"{parent_dir}/data"
        return data_dir
    else:
        raise ValueError(f"Option {option} is not found in the YAML file.")

