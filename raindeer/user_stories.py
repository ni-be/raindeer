"""
Implementation of the user stories.
"""
import logging
from typing import List
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from raindeer.dataframe_helper import dataframe_helper
import raindeer.utilities as utilities

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

show_plots = False


def fourier_analysis(data, interval, columns, case):
    """
    Perform Fourier analysis on specified columns of the data and
    plot the results.

    Args:
        data (str or pandas.DataFrame): The input data. If a string, it's
                                        assumed to be a path to a .csv file.
                                        If a DataFrame, it's used directly.

        interval (list of str): The interval at which the data is sampled.

        columns (list of str): Names of the columns in the data on which to
                               perform Fourier analysis.

        case (str): One of 'rain', 'sun', 'temp'. This decides the title and
                    units for the plot. 'rain' for Precipitation, 'sun' for
                    Sunshine, 'temp' for Temperature.

    Raises:
        AssertionError: If the input data is neither a pandas DataFrame nor a
        string, or if `case` is not one of ['rain', 'sun', 'temp'].

    """
    if isinstance(data, str) and all(isinstance(i, str) for i in interval):
        df_list = dataframe_helper(data, interval,
                                   utilities.yaml_reader('months'), 'r')
    df = df_list[0]
    # Assertion of valid inputs
    df_test = pd.DataFrame([0])
    assert type(df) == type(df_test)
    assert case in ['rain', 'sun', 'temp']

    logging.info('Performing Fourier analysis')

    # Define values for plot title and axis
    if case == 'rain':
        variable = ['Precipitation', 'mm']

    if case == 'sun':
        variable = ['Sunshine', 'W/m^2']

    if case == 'temp':
        variable = ['Temperature', 'Celsius']

    # Perform Fourier analysis on selected columns
    for column in columns:
        data = df[column].values
        n = len(data)
        dt = 1  # Assuming a constant time interval between data points of a
        # year/month

        # Perform Fourier transform
        frequencies = np.fft.fftfreq(n, dt)
        fft_values = np.fft.fft(data)

        # Plot the Fourier analysis
        plt.figure()
        plt.plot(frequencies, np.abs(fft_values))
        plt.title(f'Fourier Analysis of {column} ' + variable[0])
        plt.xlabel("Frequency")
        plt.ylabel("Magnitude in " + variable[1])
        plt.grid(True)
        if show_plots:
            plt.show()

        utilities.plot_save(plt, "user_stories", "fourier_analysis")


def linear_regression(x_data: np.ndarray, y_data: np.ndarray, x_pred: int,
                      x_label: str = 'x', y_label: str = 'y') -> float:
    """
    Predict a dependent variable using linear regression and plot the result.

    The function uses a simple linear regression model to predict 'y_data'
    values based on 'x_data' entries. It also plots the regression line.

    Args:
        x_data (np.ndarray): Independent variable values.
        y_data (np.ndarray): Dependent variable values we want to predict.
        x_pred (int): Independent variable value we want to predict for.
        x_label (str, optional): x-axis label for the plot. Default is 'x'.
        y_label (str, optional): y-axis label for the plot. Default is 'y'.

    Raises:
        AssertionError: X and Y must have the same lengths

    Returns:
        float: The predicted value for 'x_pred'.
    """
    assert len(x_data) == len(y_data), "X and Y must have the same lengths"
    num = len(x_data)
    mean_x = np.mean(x_data)
    mean_y = np.mean(y_data)

    logging.info('Performing forecast using linear regression.')
    b_1 = sum((x_data - mean_x) * (y_data - mean_y)) / sum(
        (x_data - mean_x) ** 2)
    b_0 = mean_y - b_1 * mean_x

    pred = np.zeros(num)
    for i in range(num):
        pred[i] = b_0 + b_1 * x_data[i]

    plt.plot(x_data, pred)
    plt.scatter(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if show_plots:
        plt.show()

    utilities.plot_save(plt, "user_stories", "linear_regression")
    return round(b_0 + b_1 * x_pred, 1)


def plot_data(x, y, title, x_label, y_label):
    """
    Plot y values against x values with specified labels and title.

    Args:
        x (iterable): Data to be plotted on the x-axis.
        y (iterable): Data to be plotted on the y-axis.
        title (str): Title of the plot.
        x_label (str): Label for the x-axis.
        y_label (str): Label for the y-axis.

    Returns:
        None. This function shows the plot inline and does not return any
        value.
    """
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def plot_between_years(data, interval, yearsmonths, state, case, mode):
    """
    Plot specific data between certain years in simple or custom mode.

    Args:
        data (str): Path to data or DataFrame to plot.
        interval (str/list): str or list of dates to consider for the plot.
        yearsmonths (list): 2 element list containing start , end year-month.
        state (str): Name of the state for which data should be plotted.
        case (str): Type of data to plot ('rain', 'sun', 'temp').
        mode (str): Mode of plotting ('simple', 'custom').

    Returns:
        None. Function shows the plot inline and does not return any value.

    Raises:
        ValueError: If 'case' is not in ['rain', 'sun', 'temp'],
                    or input value is of incorrect data type.
        TypeError: If input values are not numeric.

    """
    months = utilities.yaml_reader('months')
    df = []
    if isinstance(data, str) and isinstance(interval, (str, list)):
        df_list = dataframe_helper(data, interval, months, 'r')
    df = df_list[0]
    # Assertion of valid inputs
    df_test = pd.DataFrame([0])
    assert type(df) == type(df_test)
    assert case in ['rain', 'sun', 'temp']

    # Sort the dates
    df_sorted = df.sort_values('Jahr;Monat')
    cut_values = []
    cut_years = []

    logging.info('Plotting data between certain years.')

    if mode == 'simple':
        logging.info('Mode: simple')
        if case == 'rain':
            variable = ['Precipitation', 'mm']

        if case == 'sun':
            variable = ['Sunshine', 'W/m^2']

        if case == 'temp':
            variable = ['Temperature', 'Celsius']

        try:
            for yearmonth, value in zip(df_sorted["Jahr;Monat"],
                                        df_sorted[state]):

                if int(yearsmonths[0]) < int(yearmonth) < int(yearsmonths[1]):
                    cut_years.append(int(yearmonth))
                    cut_values.append(float(value))

        except ValueError:
            print('A value in the time data is not a number value')

        # Plot the results
        plt.figure()
        plt.plot(cut_years, cut_values)
        plt.title("Plot of " + variable[0] + ' ' + state)
        plt.xlabel("Date")
        plt.ylabel("Magnitude in " + variable[1])
        plt.grid(True)
        if show_plots:
            plt.show()
        utilities.plot_save(plt, "user_stories", "between_years")

    if mode == 'custom':
        logging.info('Mode: custom')
        try:
            num_plots = int(input("Enter the number of plots: "))
            num_cols = int(input("Enter the number of columns: "))

        except ValueError:
            print('A non Integer value was given, using single plot')
            num_plots = 1
            num_cols = 1

        try:
            hspacing = float(input("Enter hspace: "))
            wspacing = float(input("Enter wspace: "))

        except TypeError:
            print('A non Float value was given, using default values')
            hspacing = 0.5
            wspacing = 0.3

        # Subplots are organized in a Rows x Cols Grid
        # Tot and Cols are known
        Tot = num_plots
        Cols = num_cols

        # Compute Rows required
        Rows = Tot // Cols

        # EDIT for correct number of rows:
        # If one additional row is necessary -> add one:
        if Tot % Cols != 0:
            Rows += 1

        # Create a Position index
        Position = range(1, Tot + 1)

        # Create main figure
        fig = plt.figure(1)
        # Adjust spacing
        plt.subplots_adjust(hspace=hspacing, wspace=wspacing)

        for i in range(Tot):
            print(f"Plot {i + 1}:")
            file_path = input("Enter the path to the CSV file: ")
            x_column = input("Enter the name of the column for the x-axis: ")
            y_column = input("Enter the name of the column for the y-axis: ")

            df_custom = pd.read_csv(file_path)

            x_values = df_custom[x_column]
            y_values = df_custom[y_column]

            title = input(f"Enter title for plot {i + 1}: ")
            x_label = input(f"Enter x-axis label for plot {i + 1}: ")
            y_label = input(f"Enter y-axis label for plot {i + 1}: ")
            plot_color = input(f"Enter color for plot {i + 1}: ")

            try:
                point_size = float(
                    input(f"Enter the plot point size for plot {i + 1}: "))

            except TypeError:
                print('A non Float value was given')

            # add every single subplot to the figure with a for loop

            ax = fig.add_subplot(Rows, Cols, Position[i])
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.scatter(x_values, y_values, color=plot_color, s=point_size)

        if show_plots:
            plt.show()
        utilities.plot_save(plt, "user_stories", "between_years2")


def predict_temperature_next_year():
    """
    Predict the mean temperature in Germany for 2023.

    This function uses the linear_regression() function to estimate
    the mean temperature in Germany for 2023. The historical mean
    temperatures from 1981 to 2022 are used as the basis for the
    regression.

    Returns:
        float: The projected mean temperature in Germany for 2023.
    """
    time = range(1981, 2023)
    place = "Deutschland"

    temperature_mean = utilities.load_dataset(f"{parent_dir}/raindeer/data"
                                              f"/annual/air_temperature_mean"
                                              f"/air_temperature_mean_year.txt"
                                              ).loc[time, place].to_numpy()

    return linear_regression(time, temperature_mean, 2023,
                             'Time in years', 'Temperature mean in °C')


def plot_weather_parameters_annual(
        time: List[int] = range(1981, 2023), place: str = "Deutschland",
        data: str = f"{parent_dir}/raindeer/data/annual"):
    """
    Plots annual weather parameters (temperature, precipitation, sunshine).

    Args:
        time (List[int]): Years to show in plot. Ord, list in 1981-2023 range.
        place (str): German state or 'Deutschland'.
        data (str): Path to the data table.

    Raises:
        AssertionError: If the list of years is unsorted.

    Returns:
        None, This function shows a plot inline.

    Note:
        This function expects the 'time' list to be sorted in ascending order.
    """

    assert all(
        time[i] <= time[i + 1] for i in range(len(time) - 1)
    ), "List of years should be sorted"

    logging.info('Plotting annual weather parameters')

    temperature_mean = utilities.load_dataset(
        data + "/air_temperature_mean/air_temperature_mean_year.txt"
    ).loc[time, place]
    precipitation = utilities.load_dataset(
        data + "/precipitation/precipitation_year.txt"
    ).loc[time, place]
    sunshine_duration = utilities.load_dataset(
        data + "/sunshine_duration/sunshine_duration_year.txt"
    ).loc[time, place]

    fig, axis = plt.subplots(1, 1)
    axis.plot(temperature_mean, "r", label="Temperature")
    plt.ylabel("Temperature mean (°C)")

    axis2 = axis.twinx()
    axis2.plot(precipitation, "g", label="Rain")
    axis2.plot(sunshine_duration, "b", label="Sunshine")
    plt.ylabel("Precipitation amount (mm), sunshine duration (hrs)")

    plt.title(f"Temperature, rain, and sunshine in {place}")
    plt.xlabel("Years")
    fig.set_figwidth(15)
    fig.legend(loc="center")

    if show_plots:
        plt.show()
    utilities.plot_save(plt, "user_stories", "weather_param_annual")


def simple_plot(data, _args, mtn):
    """
    Draws plots of the given data based on specified parameters:
    Month, Bundesländer (regions in Germany), and weather phenomenon.

    Parameters:
    data: pandas DataFrame --
        The original dataset.
    -args: argparse.Namespace --
        A Namespace object from argparse. The attributes are:
            month: String --
                The specified month.
            year: Integer --
                The specified year.
            weather: List of String --
                The specified weather phenomenon identifiers.
            bundesland: List of String --
                The specified Bundesländer (regions in Germany).
    mtn: Dictionary --
        A dictionary mapping month names to their corresponding numbers.

    Outputs:
    This function plots the data based on specified parameters.
    Each plot represents a different weather phenomena like sun-duration
    or precipitation. These plots can be saved to a specified output
    file, or they will be displayed instantly.

    The plot demonstrates the observations in the specified year(s) and
    Bundesländer, across the chosen month (or annually), for the selected
    weather phenomena.
    """
    month = []
    month2 = []
    # handle input data
    if _args.month:
        interval = "monthly"
        for n in _args.month:
            month.append(n)
        for m in month:
            month2.append(mtn[m])
        index_str = "Jahr;Monat"
    else:
        interval = "annual"
        month2 = "1"
        index_str = "Jahr"

    # transform _args.month from word-strings to number-string
    if _args.month:
        i = 0
        for m in _args.month:
            _args.month[i] = mtn[m]
            i += 1
    else:
        _args.month = "0"
    df_list = dataframe_helper(_args.weather, interval, month2, "r")
    # Adding "Jahr;Monat" or "Jahr" to the dataframe
    _args.bundesland.insert(0, index_str)

    # Iterate through each entry in the df_list
    for i in range(0, len(df_list)):
        # Check if all elements in _args.bundesland exist as
        # column names in df_list[i]
        if set(_args.bundesland).issubset(df_list[i].columns):
            # Use only the required subset of Year-rows and Bundesland-Columns
            df_list[i] = df_list[i][_args.bundesland]
        else:
            print(f"Column(s)"
                  "{set(_args.bundesland) - set(df_list[i].columns)}"
                  " not found in dataframe.")
            continue  # Skip to next iteration if columns not found

        drop = []
        for row in range(0, len(df_list[i])):
            if not int(df_list[i].loc[row, index_str][0:4]) in _args.year:
                drop.append(row)
            else:
                if interval == "monthly":
                    # Avoiding chain indexing using .loc
                    df_list[i].loc[row, index_str] = \
                        df_list[i].loc[row, index_str][0:4] \
                        + "," + df_list[i].loc[row, index_str][4:6]

        df_list[i].drop(labels=drop, inplace=True)
        df_list[i].reset_index(inplace=True, drop=True)

        # Plot graphs
        df_list[i] = df_list[i].set_index([index_str])
        df_list[i] = df_list[i].astype(float)
        if i == 0:
            plot = (df_list[i].plot())
        else:
            plot = df_list[i].plot(ax=plot)

    # Process the labels
    _, legend = plot.get_legend_handles_labels()
    for i in range(0, len(legend)):
        legend[i] = _args.weather[
            i//(len(legend)//len(_args.weather))]+" "+legend[i]
        plt.legend(legend)
    if interval == "monthly":
        plt.xlabel("Jahr, Monat")

    # Save Plot
    if _args.outfile:
        try:
            plt.savefig(str(_args.outfile))
        except (ValueError):
            print("Could not save. Wrong outputfile")

    # show the graph
    plt.show()
