# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:45:01 2023

@author: timow
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/monthly/precipitation/regional_averages_tm_all.csv')

def plot_between_years(df, yearsmonths, state, case):
    # Sort the dates
    df_sorted = df.sort_values('Jahr;Monat')
    cut_values = []
    cut_years = []
    
    if case == 'rain':
        variable = ['Precipitation', 'mm']

    if case == 'sun':
        variable = ['Sunshine', 'W/m^2']

    if case == 'temp':
        variable = ['Temperature', 'Celsius']


    for yearmonth, value in zip(df_sorted['Jahr;Monat'], df_sorted[state]):
        if yearmonth > yearsmonths[0] and yearmonth < yearsmonths[1]:
            cut_years.append(yearmonth)
            cut_values.append(value)

    # Plot the results
    plt.figure()
    plt.plot(cut_years, cut_values)
    plt.title("Plot of " + variable[0] + ' ' + state)
    plt.xlabel("Date")
    plt.ylabel("Magnitude in " + variable[1])
    plt.grid(True)
    plt.show()

plot_between_years(df, [199001, 202001], 'Deutschland', 'rain')
