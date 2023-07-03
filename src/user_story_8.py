"""Functionality for user story 3: As an expert climate researcher, I want 
to make a forecast of the temperature / precipitation / sunshine duration so
that I know what the weather will be linke in the future. """

import numpy as np
import matplotlib.pyplot as plt
import utilities as utils


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
                                          "/regional_averages_tm_year.txt"
                                          ).loc[time, place].to_numpy()

    return linear_regression(time, temperature_mean, 2023,
                             'Time in years', 'Temperature mean in °C')
