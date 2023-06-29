import pandas as pd
import os
from dwd_downloader import dwd_downloader, input_checker 
from global_var import URLS, MONTHS, HEADERS, ROOT_DATA, DWD_BASE_URL # for building and testing


def dataframe_creator(season, data, interval):
   pass

def dir_check(season, data, interval):
    # TODO add a checker if season = monthly that the file for list of intervals is there
    conv_season, interval = input_checker(season, interval)
    conv_data, x  = input_checker(data, "")
    working_path = []
    data_path = []
    for list_season in conv_season:          
        working_path.append(f"{ROOT_DATA}/{list_season}")
    for data in conv_data:
        for x in working_path:
            data_path.append(f"{x}/{data}")
        

    dir_list = get_directories(working_path)
    
    not_in_dir_list = [elem for elem in data_path if elem not in dir_list]
    if len(not_in_dir_list) > 0:
        print("Missing Data will be Downloaded")
        for download in not_in_dir_list:
            pass
    else:
        return data_path


def get_directories(directory):
    directories = []
    for list_directory in directory: 
        # Iterate over the first level directories
        for root, dirs, files in os.walk(list_directory):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                directories.append(dir_path)

    return(directories)


def generate_txt_names(path, filename, iterator):
    txt_names = set()
    interval = path.split('/')[-2]
    match interval:
        case "annual":
            pass

        case "monthly":
            for i in iterator:
                txt_name = f"{path}{filename}{i}.txt"
                txt_names.add(txt_name)
    
    return txt_names

# Example usage
print(dir_check(["monthly", "annual"] , ["precipitation", "sunshine_duration"], "0"))


# Print the resulting directories
#for directory in result:
#def create_csv_from_data(path):
#    skip_rows = 3
#    temp_df = merge_files_to_dataframe(txt_files,skip_rows)
#    temp_df.to_csv(ROOT_DIR+f"/")
