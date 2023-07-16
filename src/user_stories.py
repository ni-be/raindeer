"""
Implementation of the user stories.
"""

from typing import List
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataframe_helper import dataframe_helper
import utilities

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))


def fourier_analysis(data, interval, columns, case):
    """

    :param data:
    :type data:
    :param interval:
    :type interval:
    :param columns:
    :type columns:
    :param case:
    :type case:
    :return:
    :rtype:
    """
    if isinstance(data, str) and all(isinstance(i, str) for i in interval):
        df_list = dataframe_helper(data, interval,
                                   utilities.yaml_reader('months'), 'r')
    df = df_list[0]
    # Assertion of valid inputs
    df_test = pd.DataFrame([0])
    assert type(df) == type(df_test)
    assert case in ['rain', 'sun', 'temp']

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
        plt.show()

        utilities.plot_save(plt, "user_stories", "fourier_analysis")

def linear_regression(x_data: np.ndarray, y_data: np.ndarray, x_pred: int,
                      x_label: str = 'x', y_label: str = 'y') -> float:
    """
    Function that uses a simple linear regression model to predict a
    parameter subject to another parameter and plots the linear regression
    line.
    :param x_data: The parameter X that the other parameter is depending on.
    :type x_data: numpy.ndarray
    :param y_data: The dependent parameter Y we want to predict.
    :type y_data: numpy.ndarray
    :param x_pred: The value we want to make a prediction for.
    :type x_pred: int
    :param x_label: The label for the x-axis in the plot. Defaults to 'X'.
    :type x_label: String
    :param y_label: The label for the y-axis in the plot. Defaults to 'Y'.
    :type y_label: String
    :return: The predicted value.
    :rtype: Floating point number
    """
    assert len(x_data) == len(y_data), "X and Y must have the same lengths"
    num = len(x_data)
    mean_x = np.mean(x_data)
    mean_y = np.mean(y_data)

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
    plt.show()

    utilities.plot_save(plt, "user_stories", "linear_regression")
    
    return round(b_0 + b_1 * x_pred, 1)


def plot_data(x, y, title, x_label, y_label):
    """

    :param x:
    :type x:
    :param y:
    :type y:
    :param title:
    :type title:
    :param x_label:
    :type x_label:
    :param y_label:
    :type y_label:
    :return:
    :rtype:
    """
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    

def plot_between_years(data, interval, yearsmonths, state, case, mode):
    """

    :param data:
    :type data:
    :param interval:
    :type interval:
    :param yearsmonths:
    :type yearsmonths:
    :param state:
    :type state:
    :param case:
    :type case:
    :param mode:
    :type mode:
    :return:
    :rtype:
    """
    months = utilities.yaml_reader('months')
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

    if mode == 'simple':
        if case == 'rain':
            variable = ['Precipitation', 'mm']

        if case == 'sun':
            variable = ['Sunshine', 'W/m^2']

        if case == 'temp':
            variable = ['Temperature', 'Celsius']

        try:
            for yearmonth, value in zip(df_sorted["Jahr;Monat"],
                                        df_sorted[state]):
                if yearsmonths[0] < yearmonth < yearsmonths[1]:
                    cut_years.append(yearmonth)
                    cut_values.append(value)

        except TypeError:
            print('A value in the time data is not a number value')

        # Plot the results
        plt.figure()
        plt.plot(cut_years, cut_values)
        plt.title("Plot of " + variable[0] + ' ' + state)
        plt.xlabel("Date")
        plt.ylabel("Magnitude in " + variable[1])
        plt.grid(True)
        plt.show()
        utilities.plot_save(plt, "user_stories", "between_years")
    if mode == 'custom':
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

        plt.show()
        utilities.plot_save(plt, "user_stories", "between_years2")

def predict_temperature_next_year():
    """
    Prediction of the temperature mean in Germany in 2023 using linear
    regression. (Example use of the function linear_regression() above.)
    :return: The predicted temperature mean in Germany in 2023.
    :rtype: Floating point number
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
        data: str = f"{parent_dir}/raindeer/data/annual"
):
    """
    Plots a line plot with all three parameters temperature, precipitation,
    and sunshine over time.
    :param time: List of all years shown in the plot. Should be ordered and
    years should be between 1981 and 2023.
    :type time: List[int]
    :param place: Place you want to look at. Name of a German federal state or
    'Deutschland'.
    :type place: String
    :param data: Place where the data table is found.
    :type data: String
    """
    # TODO for unittest the path needs to be relative not ../ see above
    #  root_dir and parent_dir. if not relative this will not run if run
    #  from different directory e.g not src or for unittests.

    assert all(
        time[i] <= time[i + 1] for i in range(len(time) - 1)
    ), "List of years should be sorted"

    # PROPOSED SOLUTION using dataframe helper
    # df = dataframe_helper('air_temperature_mean', 'annual', '00', True)
    # temp_df = df[df.loc[0]]
    # df = df.set_index('Jahr')
    # time_df = df[df.index.astype(float).isin(range(time[0], time[1]+1))]

    # time_df = df[df['Jahr'].astype(int).isin(range(time[0], time[1]+1))]
    # test_temperature_mean = time_df['brandenburg/berlin']

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

    plt.show()
    utilities.plot_save(plt, "user_stories", "weather_param_annual")
