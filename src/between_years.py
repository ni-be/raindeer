"""
User Story 7 between years

"""
import pandas as pd
import matplotlib.pyplot as plt
from dataframe_helper import dataframe_helper
from utilities import yaml_reader


def plot_data(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def plot_between_years(data, interval, yearsmonths, state, case, mode):
    months = yaml_reader('months')
    if isinstance(data, str) and isinstance(interval, (str, list)):
        df = dataframe_helper(data, interval, months, True)

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
            for yearmonth, value in zip(df_sorted["Jahr;Monat"],
                                        df_sorted[state]):
                if yearsmonths[0] < yearmonth < yearsmonths[1]:
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
        try:
            num_plots = int(input("Enter the number of plots: "))
            num_cols = int(input("Enter the number of columns: "))

        except ValueError:
            print('A non Integer value was given, using single plot')
            num_plots = 1
            num_cols = 1

        try:
            hspacing = float(input("Enter hspace: "))
            wspacing = float(input("Enter wspace: "))

        except TypeError:
            print('A non Float value was given, using default values')
            hspacing = 0.5
            wspacing = 0.3

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
            print(f"Plot {i + 1}:")
            file_path = input("Enter the path to the CSV file: ")
            x_column = input("Enter the name of the column for the x-axis: ")
            y_column = input("Enter the name of the column for the y-axis: ")

            df_custom = pd.read_csv(file_path)

            x_values = df_custom[x_column]
            y_values = df_custom[y_column]

            title = input(f"Enter title for plot {i + 1}: ")
            x_label = input(f"Enter x-axis label for plot {i + 1}: ")
            y_label = input(f"Enter y-axis label for plot {i + 1}: ")
            plot_color = input(f"Enter color for plot {i + 1}: ")

            try:
                point_size = float(
                    input(f"Enter the plot point size for plot {i + 1}: "))

            except TypeError:
                print('A non Float value was given')

            # add every single subplot to the figure with a for loop

            ax = fig.add_subplot(Rows, Cols, Position[i])
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.scatter(x_values, y_values, color=plot_color, s=point_size)

        plt.show()


plot_between_years("precipitation", "monthly", [177001, 202001], 'deutschland',
                   'rain', 'custom')
