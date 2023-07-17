"""
TEST FILE QUICK TESTING FUNCTIONS
"""
from raindeer.dataframe_helper import dataframe_helper
df = dataframe_helper(["precipitation"], ['monthly'], ["1"], "r")

print(df)
#selected_columns = ['deutschland']
#fourier_analysis("precipitation", "monthly", selected_columns, 'rain')