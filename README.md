# RAINDEER

Tool to analyse data from the German weather service (DWD)


This project is done as part of the Research Software Engineering course Group Project. 

* [Problem Description](#problem-description)
* [How to get started and Requirements](#how-to-get-started-requirements)
* [Running the Program](#running-the-program)
  * [CLI](#cli)
* [Dataset](#dataset)
* [Contributing](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONTRIBUTING.md)
* [Code of Conduct](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/code_of_conduct.md)
* [Licencse](https://gitup.uni-potsdam.de/jubruns/raindeer/main/LICENSE) 
* [Citation](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CITATION.cff)



# Problem Description

As part of the Project the following user stories are implemented:

## User-Stories:
1) Download tool for datasets from the Deutschen Wetter Dienst / German weather service
2) Automaticaly create dataframes and if needed download the data.
3) Fourier Analysis - TODO more details 
4) Between Years - TODO more details 
5) UserStory 3 - TODO more details 
6) Userstory 8 - TODO more details 
7) TODO Joul USER STORY 
8) TODO NIKO vertical Farming
9) TODO ? 
10) TODO ? 

# How to get Started
To install all necessary packages, run: 
```
pip install -r requirements.txt
```

## Running the Program

## Configuration and QoL

There is a config.yaml file in the root directory of the project.
You can access each list using the utilities.yaml_reader[STR_OPTION].
For more [more information](#yaml_reader)

## Jupyter Notebook

TODO Short intro and usage how and is displayed

## Module usage

### yaml_reader
For QoL purposes you can use the yaml_reader.
The yaml_reader accesses the config.yaml file in the root directory to allow easy changes to the dataset sources and headers for the dataframe. 

```Python
   utilities.yaml_reader(STR_OPTON)
```

string OPTION:
Returns a string:
root_dir = project root directory 
base_url = base url, not changing part of the download links

Returns a list:
url = urls to each dataset
headers = headers for the dataframes
months =  months 1-12
month_names = january - december
monthly_data_types = dataset that have both monthly and annual data
interval = possible intervals - annual, monthly

### plot_save

Another utility that allows easy saving of plots into the results folder.

```Python
utlities.plot_save(plt, "sub_dir", "filename")

```
This function will save plots as follows (raindeer/results/SUB_DIR/plots/FILENAME.png)

### Dataframe_helper
To work with data from the DWD you can use the dataframe helper.

```Python

import dataframe_helper as dfh

df_list = dfh_dataframe_helper(data, interval, month, "option")

# example 1: 
dataframe_helper("precipitation", "monthly", "1", "r")

# example 2:
dataframe_helper(["ice_days", "hot_days"], "annual", "0", "w")

# example 3:
dataframe_helper(["precipitation"], ["monthly", "annual"], ["01","02","03"], "r")

# if you need all months from 1-12 you can also use the utilities.yaml_reader['months']
````
Data can be either a string of a single data set or it can be a list

Possible datasets are (July 2023): 

- dataset : monthly and or annual datasets available

- air_temperature_mean: monthly, annual
- precipitation: monthly, annual
- sunshine_duration: monthly, annual
- frost_days: annual
- hot_days: annual
- ice_days: annual
- precipGE10mm: annual
- precipGE20mm: annual
- tropical_nights: annual
- summer_days: annual

For the INTERVAL as shown in the above examples use monthly and or annual. 

Month can be a single month or a list of months, in case you need only annual data you may set month to 0 as shown in example 2

Finally, the option at the end can have 3 different string values:
r : returns only a list of dataframes
w : returns a list of dataframes as well as saves a csv of combined dataframes. This is useful if you load the monthly datasets which are unfortunately initialy provided in 12 .txt files.

wcli : is mainly used automatically when accessing the dataframe_helper from the commandline. this can help to download quickly all the needed data. 

## CLI 

### Dataframe_helper - Downloader
"""BASH
$ raindeer.py --mode dataframe_helper --data_set DATA_SET --interval INTERVAL --month MONTHS
"""
DATA_SET, INTERVAL and MONTHS are the same values as above only the OPTION is not included. 

TODO add an ALL condition so that all datasets are downloaded. 
TODO URL minus BASE_URL


### TODO OTHER USER STORIES

## Datasets

### TODO DATASET DESCRIPTION


## Getting Involved

[Contributing](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CONTRIBUTING.md)
[Code of Conduct](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CONDUCT.md)


[Licencse](https://gitup.uni-potsdam.de/jubruns/raindeer/main/LICENSE) 
[Citation](https://gitup.uni-potsdam.de/jubruns/raindeer/main/CITATION.cff)
