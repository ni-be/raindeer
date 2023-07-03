"""
Functionality for user story 3: As a researcher, I want to generate a plot of
temperature , precipitation, and sunshine over time so that I can see how they
correlate.
"""

from typing import List
import matplotlib.pyplot as plt
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

    temperature_mean = utils.load_dataset(
        "../data/annual/air_temperature_mean/air_temperature_mean_year.txt"
    ).loc[time, place]

    precipitation = utils.load_dataset(
        "../data/annual/precipitation/regional_averages_rr_year.txt"
    ).loc[time, place]

    sunshine_duration = utils.load_dataset(
        "../data/annual/sunshine_duration/regional_averages_sd_year.txt"
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

    plt.draw()
