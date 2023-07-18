"""
DOWNLOADER for DWD data from the internet.
"""
import requests
import logging
from pathlib import Path
from raindeer.utilities import yaml_reader


def dwd_downloader(url_list):
    """
    Download data of the specified URL list.

    Args:
        url_list (list or string): Paths in a specific format.

     """
    logging.info('Downloading data from the specified URLs.')
    root_data = yaml_reader("root_data")
    months = yaml_reader("months")
    # convert url_list or month into lists if necessary
    url_list = input_checker(url_list)
    # iterate over the url_list
    for data in url_list:
        # Get directory from url
        time_dir = data.split('/')[-3]
        # Get sub directory from url
        sub_dir = data.split('/')[-2]
        # switch implementation for monthly or yearly
        if time_dir == "annual":
            filename = data.split('/')[-1]
            path = f"{root_data}/{time_dir}/{sub_dir}/{filename}"
            url_checker_handler(path, data)
        #elif time_dir == "monthly":
        else:
            for n in months:
                monthly_url = data.format(f"0{n}")
                filename = monthly_url.split('/')[-1]
                path = f"{root_data}/{time_dir}/{sub_dir}/{filename}"
                url_checker_handler(path, data)


def input_checker(input):
    """
    Check the input type and convert to list if necessary.

    Args:
        input: Any type of input.

    Returns:
        list: Converted input in list format.
    """
    if isinstance(input, str):
        input = string_list_converter(input)
        return input
    elif isinstance(input, list):
        return input
    else:
        input = string_list_converter(str(input))
        return input


def string_list_converter(input):
    """
    Convert the input into a list.

    Args:
        input (str): String input.

    Returns:
        list: Converted input.
    """
    conv_list = []
    conv_list += [str(input)]
    return conv_list


def url_checker_handler(path, url):
    """
    Validate URLs and handle URL errors during download.

    Args:
        path (str): Path to local file.
        url (str): DWD URL.
    """
    print(path)
    response = requests.get(url)
    if response.status_code == 200 and url.endswith('.txt'):
        content = response.text
        data_writer(path, content)
    else:
        errorfile = url.split('/')[-1]
        logging.error(f"Error downloading file: {errorfile}.")
        print(f"Error downloading file: {errorfile}.")


def data_writer(path, content):
    """
    Write downloaded data to a local file.

    Args:
        path (str): Path to local file.
        content: Content of the downloaded file.
    """
    output_file = Path(path)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(content)
    logging.info(f"Downloaded '{path}' STATUS OK.")
    print(f"Downloaded '{path}' STATUS OK.")
