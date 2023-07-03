"""Functionality for user story 3: As an expert climate researcher, I want 
to make a forecast of the temperature / precipitation / sunshine duration so
that I know what the weather will be linke in the future. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utilities as utils


def linear_regression(X: np.ndarray, Y: np.ndarray, X_pred: int,
                      X_label: str = 'X', Y_label: str = 'Y') -> float:
    """
    Function that uses a simple linear regression model to predict a
    parameter subject to another parameter and plots the linear regression
    line.
    :param X: The parameter X that the other parameter is depending on.
    :type X: numpy.ndarray
    :param Y: The dependent parameter Y we want to predict.
    :type Y: numpy.ndarray
    :param X_pred: The value we want to make a prediction for.
    :type X_pred: int
    :param X_label: The label for the x-axis in the plot. Defaults to 'X'.
    :type X_label: String
    :param Y_label: The label for the y-axis in the plot. Defaults to 'Y'.
    :type Y_label: String
    :return: The predicted value.
    :rtype: Floating point number
    """
    N = len(X)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    b_1 = sum((X - mean_X) * (Y - mean_Y)) / sum((X - mean_X) ** 2)
    b_0 = mean_Y - b_1 * mean_X

    pred = np.zeros(N)
    for i in range(N):
        pred[i] = b_0 + b_1 * X[i]

    plt.plot(X, pred)
    plt.scatter(X, Y)
    plt.xlabel(X_label)
    plt.ylabel(Y_label)
    plt.show()

    return round(b_0+b_1*X_pred, 1)


def predict_temperature_next_year():
    """
    Prediction of the temperature mean in Germany in 2023 using linear
    regression. (Example use of the function linear_regression() above.)
    :return: The predicted temperature mean in Germany in 2023.
    :rtype: Floating point number
    """
    time = range(1981, 2023)
    place = "Deutschland"

    tm = utils.load_dataset("../data/annual/air_temperature_mean"
                            "/regional_averages_tm_year.txt"
                            ).loc[time, place].to_numpy()

    return linear_regression(time, tm, 2023,
                             'Time in years', 'Temperature mean in °C')
