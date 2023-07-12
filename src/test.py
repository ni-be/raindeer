"""
TEST FILE QUICK TESTING FUNCTIONS
"""
#from dataframe_helper import dataframe_helper
#from user_stories import plot_weather_parameters_annual
from utilities import yaml_reader

# dataframe_helper(['air_temperature_mean', 'sunshine_duration',
# 'precipitation'], 'annual', '01', True)

#plot_weather_parameters_annual([1983, 2020], 'Brandenburg/Berlin',
#                               '../data/annual')
#df1, df2 = dataframe_helper(["air_temperature_mean"], ['annual','monthly'], "01", "r")

month_to = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}
#print(month_to)
print(yaml_reader("monthly_data_type"))
# yaml_string=yaml.dump(month_to)
# print("The YAML string is:")
# print(yaml_string)

#df1 = ['01', '02']
#print(df1)
#print(df2)
#print(df3)