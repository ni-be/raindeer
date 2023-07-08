"""
Implementation of the user stories.
"""

from typing import List
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import utilities as utils
from dataframe_helper import dataframe_helper

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

def plot_weather_parameters_annual(
        time: List[int] = range(1981, 2023), place: str = "Deutschland",
        data: str = f"{parent_dir}/data/annual"
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
    #TODO for unittest
    #the path needs to be relative not ../ see above root_dir and parent_dir. 
    # if not relative this will not run if run from different directory e.g not src
    # or for unittests. 
    
    assert all(
        time[i] <= time[i + 1] for i in range(len(time) - 1)
    ), "List of years should be sorted"
    
    ### PROPOSED SOLUTION using dataframe helper 
    #df = dataframe_helper('air_temperature_mean', 'annual', '00', True)
    #temp_df = df[df.loc[0]] 
    #df = df.set_index('Jahr')
    #time_df = df[df.index.astype(float).isin(range(time[0], time[1]+1))] 

    #time_df = df[df['Jahr'].astype(int).isin(range(time[0], time[1]+1))] 
    #test_temperature_mean = time_df['brandenburg/berlin']

    
    temperature_mean = utils.load_dataset(
        data + "/air_temperature_mean/air_temperature_mean_year.txt"
    ).loc[time, place]
    precipitation = utils.load_dataset(
    data + "/precipitation/precipitation_year.txt"
    ).loc[time, place]
    sunshine_duration = utils.load_dataset(
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

    return round(b_0 + b_1 * x_pred, 1)


def predict_temperature_next_year():
    """
    Prediction of the temperature mean in Germany in 2023 using linear
    regression. (Example use of the function linear_regression() above.)
    :return: The predicted temperature mean in Germany in 2023.
    :rtype: Floating point number
    """
    time = range(1981, 2023)
    place = "Deutschland"

    temperature_mean = utils.load_dataset("../data/annual/air_temperature_mean"
                                          "/air_temperature_mean_year.txt"
                                          ).loc[time, place].to_numpy()

    return linear_regression(time, temperature_mean, 2023,
                             'Time in years', 'Temperature mean in °C')
