"""
Contains utility functions used for various functionalities.
"""
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
    return data
