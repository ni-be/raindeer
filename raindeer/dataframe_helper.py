"""Functionality to create custom dataframes and store them as CSV. If
single DATA set is giving in the form of "precipitation" the data will also
be return and can directly be used.
"""

import pandas as pd
import logging
from raindeer.data_helper import data_helper
from raindeer.dwd_downloader import input_checker
from raindeer.utilities import yaml_reader


def dataframe_helper(data, interval, month_range, option):
    """
    This function helps in creating a dataframe from the provided data,
    or storing multiple dataframes in the form of CSV files.

    Args:
        data (str or list): of possible dataset types used by the Dwd.

        interval (str or list): Either "monthly" or "annual".

        month_range (str, list, or int): Nonths used DF. Annual '0' enough

        option (str): Operation mode 'w' = read + write csv , 'r' read only
                        or 'dl' to download all data or redownload all data

    Raises:
        TypeError: If the data types of the parameters are not as expected.
        ValueError: If 'data' and 'interval' parameters are not as expected.


    Returns:
        list: A list of dataframes created from the provided data.

    This function first checks the types and values of the input parameters.
    It then converts the input data into a suitable format and creates a list
    of dataframes from it. If the 'option' parameter is set to "w",
    the dataframes are also stored as CSV files.

    """
    if not isinstance(data, (str, list)):
        raise TypeError("Data parameter must be a string or a list")
    if not isinstance(interval, (str, list)):
        raise TypeError("Interval parameter must be a string or a list")
    if not isinstance(month_range, (str, list, int)):
        raise TypeError("Month range parameter must be a string, a list or "
                        "an integer")
    if not isinstance(option, str):
        raise TypeError("Option parameter must be string")
    if isinstance(data, str) and data not in ['air_temperature_mean',
                                              'frost_days',
                                              'hot_days', 'ice_days',
                                              'precipGE10mm_days',
                                              'precip20mm_days',
                                              'precipitation', 'summer_days',
                                              'sunshine_duration',
                                              'tropical_nights_tminGE20']:
        raise ValueError("Data parameter is wrong! Please check the "
                         "documentation.")
    if isinstance(interval, str) and interval not in ['monthly', 'annual']:
        raise ValueError("Interval parameter must be either 'monthly' or "
                         "'annual'")

    interval_list = input_checker(interval)
    month_list = input_checker(month_range)
    conv_data = input_checker(data)
    data_list = data_helper(conv_data, interval_list, option)
    df_ret = []
    logging.info('Creating a dataframe from the provided data')
    for dlist in data_list:
        # dlist_dt = dlist.split('/')[-1]
        interv = dlist.split('/')[-2]
        df = dataframe_creator(dlist, interv, month_list, option)
        df_ret.append(df)
    return df_ret


def dataframe_creator(data, interval, month_range, option):
    """
    This function creates a dataframe from the provided data, or stores it in
    the form of a CSV file.

    Args:
        data (str): String of possible dataset types used by the Dwd.
        interval (str): A string with either "monthly" or "annual".
        month_range (list): Defines the months used in the dataframe. Each
                            element in the list should represent a month
                            (1 for January, 2 for February, etc). This is
                            only applicable for the "monthly" interval.
        option (str): Specifies the operation mode. Use "w" for write mode
                      (to store the dataframe as a CSV file), "r" for read
                      mode (to output the dataframe only), or "wcli" for
                      write mode with more print output.

    Raises:
        ValueError: If the value of the 'interval' parameter is not in the
                    expected list.

    Returns:
        DataFrame: A dataframe created from the provided data.

    This function checks the value of the 'interval' parameter and creates a
    dataframe accordingly. If the 'option' parameter is set to "w" or "wcli",
    the dataframe is also stored as a CSV file.
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
            if len(str(months)) == 1:
                filename.append(f"{data}/{ending}_0{months}.txt")
            else:
                filename.append(f"{data}/{ending}_{months}.txt")
        df = merge_files_to_dataframe(filename, 3)
        if option == "w" or option == "wcli":
            logging.info(f"Adding {filename} adding to csv writer")
            print(f"Adding {filename} adding to csv writer")
            write_csv(df, data, ending)
    else:
        logging.error("An error has occurred in the Dataframe_creator")
        print("An error has occurred in the Dataframe_creator")
    return df


def merge_files_to_dataframe(filenames, skip_rows):
    """
    Merges txt files into a single dataframe, skips specified rows.

    Args:
        filenames (list): Path of the txt files to download.
        skip_rows (int): Number of rows to skip in the txt files.

    Returns:
        DataFrame: A dataframe merged from the txt files.
    """
    logging.info('Mergeing txt files into a single dataframe')
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
    Write the dataframe to a csv.

    Args:
        df (DataFrame): DataFrame to be written to csv.
        data (str): Descriptor for file path.
        ending (str): Descriptor for file name, i.e. "precipitation".

    This function writes the provided dataframe to a csv file at the specified
    path. The filename is constructed using the 'ending' parameter.
    """
    df.to_csv(f"{data}/{ending}_combined_data.csv",
              index=False, header=True)
    logging.info(print("Writing dataframe to a csv"))
    print(f"Wrote Dataframe as {data}/{ending}_combined_data.csv")
