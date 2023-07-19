"""Functions to do the background tasks to work efficiently with data
provided by the DWD """
import os
import logging
from raindeer.dwd_downloader import dwd_downloader
from raindeer.utilities import yaml_reader


def data_helper(conv_data, interval, option):
    """
    Retrieve all the urls and local paths for each data set.

    Args:
        conv_data (str or list): The Dataset(s) from DWD. If a list is
            provided, each item must be a string representing a dataset.
        interval (list): 'annual' and/or 'monthly'. The interval must only
            contain these values and cannot be empty.
        option (str): Must be either 'w', 'r', or 'wlci'.

    Returns:
        list: Paths that the function has computed. Each element is a string.

    Raises:
        AssertionError: If any of the above `Args:` conditions is not met,
            an AssertionError is raised with an informative error message.
    """
    assert isinstance(interval, list),\
        "interval must be a list"
    assert option in ["w", "r", "wlci"],\
        "option must be 'w', 'r', or 'wlci'"
    if isinstance(conv_data, list):
        for data in conv_data:
            assert isinstance(data, str),\
                "Each item in conv_data list must be a string"
    else:
        assert isinstance(conv_data, str),\
            "conv_data must be a string or a list of strings"

    root_data = yaml_reader("root_data")
    mon_type = yaml_reader("monthly_data_type")
    data_path = []
    for data in conv_data:
        if data in mon_type and len(interval) == 2:
            data_path.append(f"{root_data}/monthly/{data}")
            data_path.append(f"{root_data}/annual/{data}")
        elif data in mon_type and len(interval) == 1 and \
                interval[0] == "monthly":
            data_path.append(f"{root_data}/monthly/{data}")
        elif len(interval) == 1 and interval[0] == "annual":
            data_path.append(f"{root_data}/annual/{data}")
        elif data not in mon_type and interval[0] == "monthly" \
                and len(interval) == 1:
            print("Sorry, this data type does not have monthly data!")
            logging.error(f"{data}: no monthly avail.")
        else:
            print(f"for {data} no monthly data available")
    dwd_downloader(local_check(data_path, option))
    txt_renamer(data_path)
    logging.info('Data path: ' + str(data_path))
    return data_path


def txt_renamer(path):
    """
    Rename the inconsistent txt files provided by DWD.

    Args:
        path (list): data_path created in data_helper.
    """
    if not isinstance(path, list):
        raise TypeError("path must be a list")
    for pathx in path:
        data_type = pathx.split('/')[-1]
        assert isinstance(data_type, str), "data_type must be a string"

        interval_type = pathx.split('/')[-2]
        for filename in os.listdir(pathx):
            if filename.endswith((".txt", ".csv")):
                if interval_type == "monthly":
                    ending = filename[-7:]
                    rename_function(filename, data_type, ending, pathx)
                elif interval_type == "annual":
                    ending = str(filename[-9:])
                    rename_function(filename, data_type, ending, pathx)
                else:
                    print(
                        f"Interval needs to be monthly or annual, "
                        f"{interval_type} does not exists"
                    )
                    logging.error( 
                        f"Interval needs to be monthly or annual, "
                        f"{interval_type} does not exists"
                    )
            else:
                logging.error(f"File {filename} doesn't end with .txt/.csv")
                raise ValueError(
                    f"The file {filename} does not end with .txt /.csv")


def rename_function(filename, data_type, ending, path):
    """
    Rename the txt files from the DWD.

    Args:
        filename (str): Current filename.
        data_type (str): Type of the data e.g., precipitation.
        ending (str): Ending of the filename e.g., '_year.txt'.
        path (str): Directory path to the file.
    """
    # Check that all inputs are of type string
    if not isinstance(data_type, str):
        raise TypeError("data_type must be a string")
    if not isinstance(ending, str):
        raise TypeError("ending must be a string")
    if not isinstance(path, str):
        raise TypeError("path must be a string")

    # Check that ending starts with '_'
    old_filename = os.path.join(path, filename)
    if not isinstance(old_filename, str):
        raise TypeError("old_file_name must be a string")
    if not old_filename.endswith(('.txt', '.csv')):
        raise ValueError("old_file_name must end with '.txt' or .csv")

    new_name = str(data_type + ending)
    new_file = os.path.join(path, new_name)
    try:
        if os.path.exists(new_file):
            # Remove the existing file before renaming
            os.remove(new_file)
        os.rename(old_filename, new_file)
    except FileNotFoundError:
        print(f"{old_filename} does not exist")


def local_check(directory, option):
    """
    Check if dataset type exists on the filesystem.

    Args:
        directory (list): List of datatype sets including path.
        option (str): Action mode, 'w', 'r', 'wlci'.

    Returns:
        list: Download URLs.
    """
    download_list = []
    for dir in directory:
        if not os.path.exists(dir):
            logging.info(f"{dir}: not yet exists, will commence download!")
            #print(f"{dir} does not yet exists, will commence download!")
            download_list.append(dir)
        else:
            if option == "wcli":
                logging.info(f"{dir} does exist")
                #print(f"{dir} does exist")
    download_url_list = create_url_download_list(download_list)
    return download_url_list


def create_url_download_list(input):
    """
    Generate a download list based on the given input.

    Args:
        input (list): List of datatypes to be downloaded.

    Returns:
        list: Download list.
    """
    # Check that file_paths and URLS are lists
    if not isinstance(input, list):
        raise TypeError("file_paths must be a list")

    # Check that all elements in file_paths and urls are strings
    if not all(isinstance(fp, str) for fp in input):
        raise TypeError("All elements in input must be strings")

    urls = yaml_reader("urls")
    if not isinstance(urls, list):
        raise TypeError("URLS must be a list")

    indices_list = []
    url_list = []
    download_list = []
    for url in urls:
        url_list.append(url.split('/')[-2])
    for path_input in input:
        indices_list.extend(
            [index for index, value in enumerate(url_list)
             if value == path_input.split('/')[-1]])
    for index in indices_list:
        download_list.append((urls[index]))
    return download_list
