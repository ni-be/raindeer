"""
DOWNLOADER for DWD data from the internet.
"""
import requests
from pathlib import Path
from global_var import MONTHS, ROOT_DATA


def dwd_downloader(url_list):
    """
    Takes a list of paths from data_helper to download
    :param url_list: paths in the format "data/annual/precipitation"
    :type url_list: list
    """
    ## convert url_list or month into lists if necessary
    url_list = input_checker(url_list)
    months = input_checker(MONTHS)
    # iterate over the url_list
    for url in url_list:
        ## Get directory from url
        time_dir = url.split('/')[-3]
        ## Get sub directory from url
        sub_dir = url.split('/')[-2]
        #switch implementation for monthly or yearly 
        match time_dir:
            case "annual":
                filename = url.split('/')[-1]
                path = f"{ROOT_DATA}/{time_dir}/{sub_dir}/{filename}"
                url_checker_handler(path, url)
            case "monthly":
                for n in months:
                    monthly_url = url.format(n)
                    filename = monthly_url.split('/')[-1]
                    path = f"{ROOT_DATA}/{time_dir}/{sub_dir}/{filename}"
                    url_checker_handler(path, monthly_url)


def input_checker(input):
    """
    Function to check the input and convert it into a list
    :param input: any input
    :type input:  any 
    :output: list
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
    conversts input into a list
    :param input: 
    :type input: string
    """
    conv_list = []
    conv_list += [input]
    return conv_list


def url_checker_handler(path, url):
    """
    Checks whether the https urls are correct and the servers are online 
    and downloads the data if OK

    :param path: local file path 
    :type path: string
    :param url: DWD url 
    :type url: string
    """
    response = requests.get(url)
    if response.status_code == 200 and url.endswith('.txt'):
        content = response.text
        data_writer(path, content) 
    else:
        errorfile = url.split('/')[-1]
        print(f"Error downloading file: {errorfile}.")
        

def data_writer(path, content):
    """
    writes the data into local files
    :param path: local file path
    :type path: string
    :param content: content of the txt file
    :type web content? 
    """
    output_file = Path(path)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(content)
    print(f"Downloaded '{path}' STATUS OK.")


