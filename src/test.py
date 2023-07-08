import pandas as pd
from dataframe_helper import dataframe_helper
from utilities import yaml_reader

months = yaml_reader('months')
df = dataframe_helper("precipitation", "monthly", months, True)

#print(df)
