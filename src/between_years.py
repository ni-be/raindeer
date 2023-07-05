# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:45:01 2023

@author: timow
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('../data/monthly/precipitation/regional_averages_tm_all.csv')


def plot_data(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def plot_between_years(df, yearsmonths, state, case, mode):

    # Assertion of valid inputs
    df_test = pd.DataFrame([0])
    assert type(df) == type(df_test)
    assert case in ['rain', 'sun', 'temp']

    # Sort the dates
    df_sorted = df.sort_values('Jahr;Monat')
    cut_values = []
    cut_years = []

    if mode == 'simple':
        if case == 'rain':
            variable = ['Precipitation', 'mm']

        if case == 'sun':
            variable = ['Sunshine', 'W/m^2']

        if case == 'temp':
            variable = ['Temperature', 'Celsius']

        try:
            for yearmonth, value in zip(df_sorted['Jahr;Monat'],
                                        df_sorted[state]):
                if yearmonth > yearsmonths[0] and yearmonth < yearsmonths[1]:

                    cut_years.append(yearmonth)
                    cut_values.append(value)

        except TypeError:
            print('A value in the time data is not a number value')

        # Plot the results
        plt.figure()
        plt.plot(cut_years, cut_values)
        plt.title("Plot of " + variable[0] + ' ' + state)
        plt.xlabel("Date")
        plt.ylabel("Magnitude in " + variable[1])
        plt.grid(True)
        plt.show()

    if mode == 'custom':
        num_plots = int(input("Enter the number of plots: "))
        num_cols = int(input("Enter the number of columns: "))
        hspacing = float(input("Enter hspace: "))
        wspacing = float(input("Enter wspace: "))

        # Subplots are organized in a Rows x Cols Grid
        # Tot and Cols are known
        Tot = num_plots
        Cols = num_cols

        # Compute Rows required
        Rows = Tot // Cols

        # EDIT for correct number of rows:
        # If one additional row is necessary -> add one:
        if Tot % Cols != 0:
            Rows += 1

        # Create a Position index
        Position = range(1, Tot + 1)

        # Create main figure
        fig = plt.figure(1)
        # Adjust spacing
        plt.subplots_adjust(hspace=hspacing, wspace=wspacing)

        for i in range(Tot):
            print(f"Plot {i+1}:")
            file_path = input("Enter the path to the CSV file: ")
            x_column = input("Enter the name of the column for the x-axis: ")
            y_column = input("Enter the name of the column for the y-axis: ")

            df_custom = pd.read_csv(file_path)

            x_values = df_custom[x_column]
            y_values = df_custom[y_column]

            title = input(f"Enter title for plot {i+1}: ")
            x_label = input(f"Enter x-axis label for plot {i+1}: ")
            y_label = input(f"Enter y-axis label for plot {i+1}: ")
            plot_color = input(f"Enter color for plot {i+1}: ")

            # add every single subplot to the figure with a for loop

            ax = fig.add_subplot(Rows, Cols, Position[i])
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.scatter(x_values, y_values, color=plot_color)

        plt.show()


plot_between_years(df, [177001, 202001], 'Deutschland', 'rain', 'custom')
