"""
TEST FILE QUICK TESTING FUNCTIONS
"""
from dataframe_helper import dataframe_helper
from user_stories import fourier_analysis


df = dataframe_helper(["frost_days"], ['annual'], ["0"], "r")

print(df)
#selected_columns = ['deutschland']
#fourier_analysis("precipitation", "monthly", selected_columns, 'rain')

