"""Functionality to create custom dataframes and store them as CSV. If
single DATA set is giving in the form of "precipitation" the data will also
be return and can directly be used. """
import pandas as pd
from data_helper import data_helper
from dwd_downloader import input_checker
from utilities import yaml_reader


def dataframe_helper(data, interval, month_range, option):
    """
    Takes data parameter and returns a dataframe,
        or stores multiple in form of csv
    :param data: takes either a list or string of possible dataset types
        used by the Dwd.
    :type data: String or list[]
    :param interval: takes either a string or list with either of the following
        two parameters "monthly" or "annual"
    :type interval: String or list[]
    :param month_range: define the months used in dataframe
        > only for interval monthly
    :type month_range: string or list or int
    :format month_range: 01, 02, 03, ... 12
    :param option is True or False - True for Write CSV and False for return DF
     only
    :type option: BOOL
    """
    if not isinstance(data, (str, list)):
        raise TypeError("Data parameter must be a string or a list")
    if not isinstance(interval, (str, list)):
        raise TypeError("Interval parameter must be a string or a list")
    if not isinstance(month_range, (str, list, int)):
        raise TypeError("Month range parameter must be a string, a list or "
                        "an integer")
    if not isinstance(option, bool):
        raise TypeError("Option parameter must be boolean")
    if isinstance(data, str) and data not in ['air_temperature_mean',
                                              'frost_days',
                                              'hot_days', 'ice_days',
                                              'precipGE10mm_days',
                                              'precip20mm_days',
                                              'precipitation', 'summer_days',
                                              'sunshine_duration',
                                              'tropical_nights_tminGE20']:
        raise ValueError("Data parameter is wrong! Please check the "
                         "documenation.")
    if isinstance(interval, str) and interval not in ['monthly', 'annual']:
        raise ValueError("Interval parameter must be either 'monthly' or "
                         "'annual'")

    interval_list = input_checker(interval)
    month_list = input_checker(month_range)
    data_list = data_helper(data, interval_list)

    if len(data_list) == 1 and len(interval_list) == 1:
        df = dataframe_creator(data_list[0], interval_list[0], month_list,
                               option)
        return df
    elif len(data_list) > 1 and len(interval_list) == 1:
        for data in data_list:
            df = dataframe_creator(data, interval_list[0], month_list, option)
        return df
    elif len(data_list) == 1 and len(interval_list) > 1:
        for interval in interval_list:
            df = dataframe_creator(data_list[0], interval, month_list, option)
            return df
    elif len(data_list) > 1 and len(interval_list) > 1 and option == True:
        for interval in interval_list:
            for data in data_list:
                dataframe_creator(data, interval, month_list, option)
    else:
        print(f" Data List: {data_list}, Interval List {interval_list} \
                        or Month List: {month_list} seem to be empty!")


def dataframe_creator(data, interval, month_range, option):
    """
    Takes data parameter and returns a dataframe,
        or stores multiple in form of csv
    :param data: is astring of possible dataset types used by the Dwd.
    :type data: String
    :param interval: takes a string with either of the following
        two parameters "monthly" or "annual"
    :type interval: String
    :param month_range: define the months used in dataframe
        > only for interval monthly
    :type month_range: list
    :format month_range: 01, 02, 03, ... 12
    :param option: Write to csv yes or no
    :type option : BOOL
    """

    if interval not in ['monthly', 'annual']:
        raise ValueError(f"Invalid interval: {interval}. Interval must \
                         be either monthly or annual.")
    df = pd.DataFrame()
    filename = []
    if str(interval) == "annual":
        ending = data.split('/')[-1]
        filename.append(f"{data}/{ending}_year.txt")
        annual_df = merge_files_to_dataframe(filename, 3)
        annual_df = annual_df.applymap(lambda x: x.replace('year', ''))
        df = annual_df.rename(columns=lambda x: x.replace(';Monat', ''))
    elif str(interval) == "monthly":
        for months in month_range:
            ending = data.split('/')[-1]
            filename.append(f"{data}/{ending}_{months}.txt")
        df = merge_files_to_dataframe(filename, 3)
        if option is True:
            print("adding to csv writer")
            write_csv(df, data, ending)
    else:
        print("An error has occurred in the Dataframe_creator")
    return df


def merge_files_to_dataframe(filenames, skip_rows):
    """
    Merges txt files in a directory into a single dataframe, with dropping the
    top 3 rows.
    :param filenames:  is the path of the txt files to download
    :type filenames: list
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
    df.columns = yaml_reader('headers')
    # Remove ; from all cells
    for col in df.columns:
        df[col] = df[col].str.replace(';', '')
    return df


def write_csv(df, data, ending):
    """
    Write the dataframe to a csv
    :param data:
    :type data:
    :param df: dataframe
    :type df: dataframe
    :param ending: descriptor of for file name i.e. "precipitation"
    :type ending: string
    """
    df.to_csv(f"{data}/{ending}_combined_data.csv",
              index=False, header=True)
    print(f"Wrote Dataframe as {data}/{ending}_combined_data.csv")

# Debug statement TODO REMOVE
# dataframe_helper(['ice_days'], ['annual'], ['01'], True)
