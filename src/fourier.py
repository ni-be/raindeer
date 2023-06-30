# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:15:05 2023

@author: timow
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/monthly/precipitation/regional_averages_tm_all.csv')

def fourier_analysis(df, columns, case):

    if case == 'rain':
        variable = ['Precipitation', 'mm']

    if case == 'sun':
        variable = ['Sunshine', 'W/m^2']

    if case == 'temp':
        variable = ['Temperature', 'Celsius']

    # Perform Fourier analysis on selected columns
    for column in columns:
        data = df[column].values
        n = len(data)
        dt = 1  # Assuming a constant time interval between data points of a year/month

        # Perform Fourier transform
        frequencies = np.fft.fftfreq(n, dt)
        fft_values = np.fft.fft(data)

        # Plot the Fourier analysis
        plt.figure()
        plt.plot(1/frequencies, np.abs(fft_values))
        plt.title(f'Fourier Analysis of {column} ' + variable[0])
        plt.xlabel("1/Frequency")
        plt.ylabel("Magnitude in " + variable[1])
        plt.xlim(2, 12)
        plt.grid(True)
        plt.show()


# Example usage:
# Assuming you have a DataFrame called 'df' with columns 'column1' and 'column2'
selected_columns = ['Deutschland']
fourier_analysis(df, selected_columns, 'rain')