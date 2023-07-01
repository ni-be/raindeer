import pandas as pd
import os
from dwd_downloader import dwd_downloader, input_checker
from global_var import URLS, MONTHLY_DATA_TYPE, INTERVAL, ROOT_DATA,MONTHS


def dataframe_creator(data, months):
    data_list_path = dir_check(data)
    months_list = input_checker(months)
    generate_txt_names(data_list_path, months_list)
    print(data_list_path)
    

def csv_creator():
    #df.to_csv("")
    pass


def generate_txt_names(data_path, iterator):
    txt_names = []
    for data in data_path:
        interval = data_path.split('/')[-2]
        file_name = data_path.split('/')[-1] 
        match interval:
            case "annual":
                pass
            case "monthly":
                for i in iterator:
                    txt_name = f"{data}/{file_name}_monthly_{i}.txt"
                    txt_names.append(txt_name) 
    return txt_names


def txt_renamer(path):
    for pathx in path:
        data_type = pathx.split('/')[-1]
        interval_type = pathx.split('/')[-2]
        for filename in os.listdir(pathx):
            # Check if the file has a text file extension
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
    old_filename = os.path.join(path, filename)
    new_name = str(data_type + ending)
    new_file = os.path.join(path, new_name)
    try: 
        os.rename(old_filename, new_file)
    except FileNotFoundError:
        print(f"{old_filename} does not exist")


def dir_check(data):
    # Check whether data is already downloaded or not, if not download it. 
    conv_data  = input_checker(data)
    data_path = [] 
    for data in conv_data:
        if data in MONTHLY_DATA_TYPE:
            data_path.append(f"{ROOT_DATA}/monthly/{data}")
            data_path.append( f"{ROOT_DATA}/annual/{data}")
        else: 
            data_path.append(f"{ROOT_DATA}/annual/{data}")
    dwd_downloader(local_check(data_path))
    txt_renamer(data_path)
    return data_path


def valid_dir_check_from_url(input):
    data_url = []
    interval_url = []
    data_indices_list = []
    interval_indices_list = [] 
    for url in URLS:
        data_url.append(url.split('/')[-2])
        interval_url.append(url.split('/')[-3])
    for path_input in input:
        data_indices_list.extend(
            [index for index, value in enumerate(data_url)
            if value == path_input])
        interval_indices_list.extend(
            [index for index, value in enumerate(interval_url)
            if value == path_input])


def create_url_download_list(input):
    indices_list = []
    url_list = []
    download_list = []
    for url in URLS:
        url_list.append(url.split('/')[-2])
    for path_input in input:    
        indices_list.extend(
            [index for index, value in enumerate(url_list)
            if value == path_input.split('/')[-1]]
        ) 
    for index in indices_list:
        download_list.append((URLS[index]))
    return download_list


def local_check(directory):
    download_list = []
    for dir in directory:
        if not os.path.exists(dir):
            print(f"{dir} does not yet exists, will commence download!")
            download_list.append(dir)
        else:
            print(f"{dir} does exist")

    download_url_list = create_url_download_list(download_list)
    return download_url_list


# TESTING Example usage
#dataframe_creator(["precipitation", "sunshine_duration", "hot_days"], ["01","03"])
txt_renamer(["../data/monthly/precipitation"])
