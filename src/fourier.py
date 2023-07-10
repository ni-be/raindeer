"""
User Story ? Fourier analysis: 
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataframe_helper import dataframe_helper
from utilities import yaml_reader


def fourier_analysis(data, interval, columns, case):
    
    if isinstance(data, str) and isinstance(interval, str):
        df = dataframe_helper(data, interval, yaml_reader('months'), False)
    
    # Assertion of valid inputs
    df_test = pd.DataFrame([0])
    assert type(df) == type(df_test)
    assert case in ['rain', 'sun', 'temp']

    # Define values for plot title and axis
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
        dt = 1  # Assuming a constant time interval between data points of a
        # year/month

        # Perform Fourier transform
        frequencies = np.fft.fftfreq(n, dt)
        fft_values = np.fft.fft(data)

        # Plot the Fourier analysis
        plt.figure()
        plt.plot(frequencies, np.abs(fft_values))
        plt.title(f'Fourier Analysis of {column} ' + variable[0])
        plt.xlabel("Frequency")
        plt.ylabel("Magnitude in " + variable[1])
        plt.grid(True)
        plt.show()


# Example usage: Assuming you have a DataFrame called 'df' with columns
# 'column1' and 'column2'
selected_columns = ['deutschland']
fourier_analysis("precipitation", "monthly", selected_columns, 'rain')
