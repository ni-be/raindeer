"""
Functionality for user story 3: As a researcher, I want to generate a plot of
temperature , precipitation, and sunshine over time so that I can see how they
correlate.
"""

import matplotlib.pyplot as plt
from typing import List
import utilities as utils


def plot_weather_parameters_annual(
        time: List[int] = range(1981, 2023), place: str = "Deutschland"
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
    """
    assert all(
        time[i] <= time[i + 1] for i in range(len(time) - 1)
    ), "List of years should be sorted"

    tm = utils.load_dataset(
        "../data/annual/air_temperature_mean/regional_averages_tm_year.txt"
    ).loc[time, place]

    rr = utils.load_dataset(
        "../data/annual/precipitation/regional_averages_rr_year.txt"
    ).loc[time, place]

    sd = utils.load_dataset(
        "../data/annual/sunshine_duration/regional_averages_sd_year.txt"
    ).loc[time, place]

    fig, ax = plt.subplots(1, 1)
    ax.plot(tm, "r", label="Temperature")
    plt.ylabel("Temperature mean (°C)")

    ax2 = ax.twinx()
    ax2.plot(rr, "g", label="Rain")
    ax2.plot(sd, "b", label="Sunshine")
    plt.ylabel("Precipitation amount (mm), sunshine duration (hrs)")

    plt.title("Temperature, rain, and sunshine in {}".format(place))
    plt.xlabel("Years")
    fig.set_figwidth(15)
    fig.legend(loc="center")

    plt.draw()
