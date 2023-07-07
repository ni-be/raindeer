"""
Functions to do the background tasks to work efficiently with data provided by the DWD
"""
import os
from dwd_downloader import dwd_downloader, input_checker
from utilities import yaml_reader


def data_helper(data):
    """
    Function that takes the data to find all the urls and local paths for each set.
    Returns a list of paths 
    :param data: contains a string or list of possible dataset from DWD
    :type data: String or List
    """
    root_data = yaml_reader("root_data")
    monthly_data_type = yaml_reader("monthly_data_type")
    conv_data  = input_checker(data)
    data_path = [] 
    for data in conv_data:
        if data in monthly_data_type:
            data_path.append(f"{root_data}/monthly/{data}")
            data_path.append( f"{root_data}/annual/{data}")
        else: 
            data_path.append(f"{root_data}/annual/{data}")
    dwd_downloader(local_check(data_path))
    txt_renamer(data_path)
    return data_path


def txt_renamer(path):
    """
    DWD provided txt files have inconsistent file names,
    txt_renamer is used to rename the txt files after downloading 
    :param path: takes the data_path created in data_helper as input
    :type path: list
    """
    for pathx in path:
        data_type = pathx.split('/')[-1]
        interval_type = pathx.split('/')[-2]
        for filename in os.listdir(pathx):
            if filename.endswith(".txt"):
                if interval_type == "monthly":
                    ending = filename[-7:]
                    rename_function(filename, data_type, ending, pathx)
                elif interval_type == "annual":
                    ending = str(filename[-9:])
                    rename_function(filename, data_type, ending, pathx)
                else:
                    print(f"Internval needs to be monthly or annual, {interval_type},\
                            does not exists")


def rename_function(filename, data_type, ending, path):
    """
    Function to effectively rename the txt files
    :param filename: current filename
    :type filename: String
    :param data_type: precipitation etc
    :type data_type: String
    :param ending: _year.txt for annual  _01.txt for monthly
    :type ending: String
    :param path: directory path to file
    :type path: String
    """
    old_filename = os.path.join(path, filename)
    new_name = str(data_type + ending)
    new_file = os.path.join(path, new_name)
    try: 
        os.rename(old_filename, new_file)
    except FileNotFoundError:
        print(f"{old_filename} does not exist")


def local_check(directory):
    """
    Checks whether or not a dataset type is already present on the filesystem, if not
    path will be added to the downloadlist and run through the create_url_download list
    :param directory: list of datatype sets including path
    :type directory: list
    """
    download_list = []
    for dir in directory:
        if not os.path.exists(dir):
            print(f"{dir} does not yet exists, will commence download!")
            download_list.append(dir)
        else:
            print(f"{dir} does exist")
    download_url_list = create_url_download_list(download_list)
    return download_url_list


def create_url_download_list(input):
    """
    As part of the local_check this function does the creation of the download list
    checks whether a combination of datatype and interval type exists and if yes
    adds it to the download list precipitation monthly or annual only? 
    :param input: list of datatypes to download
    :type input: list

    """
    urls = yaml_reader("urls")
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

