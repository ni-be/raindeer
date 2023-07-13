"""
TEST FILE QUICK TESTING FUNCTIONS
"""
from dataframe_helper import dataframe_helper
from user_stories import fourier_analysis


df = dataframe_helper(["air_temperature_mean"], ['annual','monthly'], "1", "r")

selected_columns = ['deutschland']
fourier_analysis("precipitation", "monthly", selected_columns, 'rain')

