# Raindeer

Analysis of weather data in Germany. 

This project is done as part of the _Research Software Engineering_ course 
group project in summer 2023. 

* [Problem description](#problem-description)
* [How to get started](#how-to-get-started)
* [Running the program](#running-the-program)
* [Configuration and QoL](#configuration-and-qol)
* [Jupyter Notebook](#jupyter-notebook)
* [Module usage](#module-usage)
* [Command-line interface](#command-line-interface)
* [Dataset](#dataset)
* [How to get involved](#how-to-get-involved)



## Problem description

### Research questions
This project was created on the basis of answering the following research questions:

1) What is the temperature trend in germany?
2) Are there correlations between different weather parameters?
3) What will the average temperature be next year in germany?
4) Are there patterns in the weather data?
5) How can we make the weather data from the online database usable?

From these, multiple user stories were created:

### User-Stories:
1. As a researcher, I want to generate a plot of temperature, precipitation, and sunshine over time so that I can see how they correlate.
2. As a researcher, I want to plot the temperature, precipitation, and sunshine duration of a federal state in a certain time frame so that I can better understand the correlations between these weather phenomenons.
3. As a researcher, I want to plot the yearly mean temperature, precipitation, or sunshine duration of different federal states so that I can have a more general understanding of the differences in climate between them.
4. As a researcher, I want to be able to save resulting plots and images so that I can easily use them in, for example, research papers.
5. As an expert researcher, I want to be able to customize a lot so that the result fits my specific research question.
6. As a researcher, I want to be able to view patterns in the weather conditions such as reoccurring events and their frequency.
7. As a climate researcher, I want to automatically download data from the German Meteorological Service so that I do not waste time doing this by hand.
8. As an expert climate researcher, I want to make a forecast of the temperature / precipitation / sunshine duration so that I know what the weather will be like in the future.
9. ...

[Here](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/docs/requirements.md) you can find a full list of all user stories. Some of which are not yet implemented.

## How to get started
After downloading this package, install it by running the following command in its root directory:
```BASH
$ pip install -e .
```
In addition you may get started with running the following little helper: 
```BASH
$ chmod +x ./little_helper.sh
$ bash ./little_helper.sh 
```
This script will install raindeer, download all the data, run unittests using coverage and will run tokei if installed. THIS SCRIPT WAS SOLOLY CREATED to make our life easier when testing and for the examiner. 

The results from past runs can be found here:

[Results](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/results/results.md)

## UNITTESTS

It is advised to either use the script above to start UNITTEST or follow the following steps manually
1. install Raindeer
2. download all the data -> 
```BASH
  $ raindeer --mode download all
```
3. Then run Unittests. with 
```BASH
$ python -m unittest
```

## Running the program
The programm has two interfaces / access points. You can access some functionality through the [command-line interface](#command-line-interface).
In addition, you can directly access the modules through importing it, e.g. to a Jupyter Notebook. 

## Configuration and QoL

There is a `config.yaml` file in the root directory of the project.
You can access each list using `utilities:yaml_reader(OPTION)`.

[More information](#yaml_reader)

## Jupyter Notebook

Start the jupyter notebook from the command-line with 
```BASH
$ jupyter notebook
```
This will open a homepage in your browser containing all files in your current working directory. From here, select ``raindeer.ipynb`` and open it. Inside the notebook is the computational narrative for this software. It explains all the modules and use-cases as well as answering some interesting research questions using the data.

## Module usage

### `yaml_reader`
For QoL purposes, you can use the `yaml_reader`.
The `yaml_reader` accesses the `config.yaml` file in the root directory to allow easy changes to the dataset sources and headers for the dataframe. 

```Python
utilities.yaml_reader(OPTION)
```

Args:
- OPTION (str) : Data point in config.yaml that is to be read.


### `plot_save`

Another utility that allows easy saving of plots into the results folder.

```Python
utilities.plot_save(PLT, "SUB_DIR", "FILENAME")
```
Args:
- PLT (matplotlib.pyplot) : The configured matplotlib plot to be saved. 
- SUB_DIR (str) : The subdirectory the plot is going to be saved in.
- FILENAME (str) : The name of the file the plot is going to be saved in.

This function will save plots as follows:
`raindeer/results/SUB_DIR/plots/FILENAME.png`.

### `dataframe_helper`
To work with data from Deutscher Wetterdienst (DWD), you can use the dataframe helper.

```Python
import raindeer.dataframe_helper as dfh

df_list = dfh_dataframe_helper(DATA, INTERVAL, MONTH, OPTION)

# example 1: 
dataframe_helper("precipitation", "monthly", "1", "r")

# example 2:
dataframe_helper(["ice_days", "hot_days"], "annual", "0", "w")

# example 3:
dataframe_helper(["precipitation"], ["monthly", "annual"], ["01","02","03"], "r")

# if you need all months from 1-12 you can also use the utilities.yaml_reader['months']
```
DATA can be either a string of a single data set or a list

Possible datasets are (July 2023): 
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

For the INTERVAL use monthly and or annual (as shown in the above examples). 

MONTH can be a single month or a list of months. In case you need only annual data, you may set month to 0 as shown in example 2.

Finally, the OPTION at the end can have 3 different string values:
- 'r' : returns only a list of dataframes
- 'w' : returns a list of dataframes as well as saves a csv of combined dataframes. This is useful if you load the monthly datasets which are unfortunately initially provided in 12 .txt files.
- 'wcli' : is mainly used automatically when accessing the dataframe_helper from the command-line. This can help to download all the needed data quickly. 
- 'dl' : download data / redownload data

An auto update was not included because data might change online. 

## Command-line interface

### `download all` - quick downloader
```BASH
$ raindeer --mode download-all 
  
```
Will download all data-sets

### `dataframe_helper` - Downloader
```BASH
$ raindeer --mode dataframe_helper --data_set DATA_SET --interval INTERVAL --month MONTHS
```
DATA_SET, INTERVAL and MONTHS are the same values as above only the OPTION is not included.

### Forecast
```BASH
$ raindeer "data/annual/air_temperature_mean/regional_averages_tm_year.txt" --mode forecast -b=BUNDESLAND -f=YEAR
```

Args:
- `--bundesland`, `-b` : German federal state the forecast is to be made for.
- `--forecast`, `-f` : The year that is to be forecast.

### Fourier
```BASH
$ raindeer WEATHER --mode fourier -b BUNDESLAND
```

Args:
- `WEATHER` : type of weather to analyse between 
  - "precipitation", 
  - "air_temperature_mean" and 
  - "sunshine".
- `--interval`, `-i` : can be set to "annual" or "monthly" to switch between the datasets.
- `--bundesland`, `b` : Takes one or more German federal states.

### Plot weather parameters annual
```BASH
$ raindeer "data/annual" --mode plot-params -b BUNDESLAND -y YEARS
````

Args:
- ``--bundesland``, `-b` : Takes one or more German federal states.
- ``--year``, `-y`:  Takes a lis.bt of years to be plotted like `"START..END"` or with ``+`` for only certain years

### Customizable plotting
```BASH
$ raindeer WEATHER --mode between-years -m MONTH  -b BUNDESLAND -w WEATHER -y START..END
```

Args:
- ``--bundesland``, `-b` : Takes a german federal state.
- ``--weather``, `-w` : Type of weather to analyse between 
  - "precipitation", 
  - "air_temperature_mean" and 
  - "sunshine".
- ``--month``, `-m` : Takes one or multiple months with ``+``to be plotted.
-  ``--complexity``, `-c` : can be set to "simple" or "custom". If "custom" is chosen, the user can freely control a vast range of parameters of the plot. This will be asked by the software as user input in the command-line.

## Authors
- Nikolas Bertrand (backend developer)
- Julian Bruns (backend developer)
- Josephine Funken (backend developer / tester)
- Timo Wedding (backend developer / “client” developer)


## How to get involved

[Contributing](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONTRIBUTING.md)

[Code of Conduct](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CONDUCT.md#contributor-covenant-code-of-conduct)

[License](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/LICENSE.txt) 

[Citation](https://gitup.uni-potsdam.de/jubruns/raindeer/-/blob/main/CITATION.cff)
