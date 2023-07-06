"""
Functionality to create custome dataframes and store them as CSV. 
If single DATA set is givin in the form of "precipitation" the data will also be 
return and can directly be used. 
"""
import pandas as pd
from data_helper import data_helper
from dwd_downloader import input_checker
from yaml_reader import yaml_reader


ROOT_DATA = yaml_reader("root_data")
HEADERS = yaml_reader("headers")


def dataframe_helper(data, interval, month_range, option):
    """
    Takes data parameter and returns a dataframe, 
        or stores multiple in form of csv
    :param data: takes either a list or string of possible dataset types 
        used by the Dwd.
    :type data: String or list[]
    :param interval: takes either a string or list with the either of following 
        two parameters "monthly" or "annual"
    :type interval: String or list[]
    :param month_range: define the months used in dataframe 
        > only for interval monthly
    :type month_range: string or list or int 
    :format month_range: 01, 02, 03, ... 12
    :param option is True or False - True for Write CSV and False for return DF only
    :type option: BOOL
    """
    interval_list = input_checker(interval)
    month_list = input_checker(month_range)
    data_list = data_helper(data)
    
    if len(data_list) == 1 and len(interval_list) == 1:
        df = dataframe_creator(data_list[0], interval_list[0], month_list, option)
        return df
    elif len(data_list) > 1 and len(interval_list) == 1: 
        for data in data_list:
            dataframe_creator(data, interval_list[0], month_list, option)
    elif len(data_list) == 1 and len(interval_list) > 1:
        for interval in interval_list:
            dataframe_creator(data_list[0], interval, month_list, option)
    elif len(data_list) >1 and len(interval_list)> 1:
        for interval in interval_list:
            for data in data_list:
                dataframe_creator(data, interval, month_list, option)
    else: 
        print(f" Data List: {data_list}, Interval List {interval_list} \
                        or Month List: {month_list} seem to be empty!")
    

def dataframe_creator(data, interval,month_range, option):
    """
    Takes data parameter and returns a dataframe, 
        or stores multiple in form of csv
    :param data: is astring of possible dataset types used by the Dwd.
    :type data: String 
    :param interval: takes a string with the either of following 
        two parameters "monthly" or "annual"
    :type interval: String
    :param month_range: define the months used in dataframe 
        > only for interval monthly
    :type month_range: list  
    :format month_range: 01, 02, 03, ... 12
    :param option: Write to csv yes or no 
    :type option : BOOL
    """
    df = pd.DataFrame()
    filename = []
    if data.split('/')[-2] == "annual":
        ending = data.split('/')[-1]
        filename.append(f"{data}/{ending}_year.txt")
        combined_annual_df = merge_files_to_dataframe(filename, 3)
        anual_df = combined_annual_df.applymap(lambda x: x.replace('year', ''))
        df = anual_df.rename(columns=lambda x: x.replace(';Monat', ''))
    elif data.split('/')[-2] == "monthly":
        for months in month_range:
            ending = data.split('/')[-1]
            filename.append(f"{data}/{ending}_{months}.txt")
        df = merge_files_to_dataframe(filename, 3)     
    else: 
        print("An error has occured in the Dataframe_creator")

    if option is True:
        write_csv(df, data, ending)
    return df


def merge_files_to_dataframe(filenames, skip_rows):
    """
    Merges txt files in a directory into a single dataframe, with dropping the 
    top 3 rows.
    :param filename: is the path of the txt files to download
    :type filename: list
    :param skip_rows the amount of rows to skip, 
    :type skip_rows: int
    """
    data = []
    for filename in filenames:
        with open(filename, 'r') as file:
            for _ in range(skip_rows):
                next(file)  # Skip the specified number of rows
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:
                    data.append(line.split())
    # Create DataFrame from the data
    df = pd.DataFrame(data)
    df.columns = [HEADERS]
    # Remove ; from all cells
    for col in df.columns:
        df[col] = df[col].str.replace(';', '')
    return df


def write_csv(df,data, ending):
    """
    Write the dataframe to a csv 
    :param df: dataframe
    :type df: dataframe
    :param ending: descriptor of for file name i.e. "precipitation"
    :type ending: string 
    """
    df.to_csv(f"{ROOT_DATA}/{ending}_combined_data.csv", index=False, header=True)
    print(f"Wrote Dataframe as {data}/{ending}_combined_data.csv")
 
