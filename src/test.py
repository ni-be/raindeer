"""
TEST FILE QUICK TESTING FUNCTIONS
"""
from dataframe_helper import dataframe_helper
from user_stories import plot_weather_parameters_annual
#dataframe_helper(['air_temperature_mean', 'sunshine_duration', 'precipitation'], 'annual', '01', True)

#plot_weather_parameters_annual([1983, 2020], 'Brandenburg/Berlin', '../data/annual')

dataframe_helper("air_temperature_mean", "annual", "01", True)

