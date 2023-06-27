# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:02:04 2023

@author: timow
"""
from global_var import MONTHS
import pandas as pd


merge = True

def generate_txt_names(base_name, iterator):
    txt_names = set()
    for i in iterator:
        txt_name = f"{base_name}{i}.txt"
        txt_names.add(txt_name)
    return txt_names


def merge_files_to_dataframe(filenames, skip_rows):
    data = []
    for filename in filenames:
        with open(filename, 'r') as file:
            for _ in range(skip_rows):
                next(file)  # Skip the specified number of rows
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:
                    data.append(line.split())

    # Create DataFrame from the data
    df = pd.DataFrame(data)
    df.columns = [row_headers]

    # Remove ; from all cells
    for col in df.columns:
        df[col] = df[col].str.replace(';', '')

    return df


# Example usage:
# Generate txt files
txt_files = generate_txt_names('../data/regional_averages_tm_', MONTHS)
row_headers = ['Jahr;Monat', 'Brandenburg/Berlin',
               'Brandenburg', 'Baden-Wuerttemberg', 'Bayern', 'Hessen',
               'Mecklenburg-Vorpommern', 'Niedersachsen',
               'Niedersachsen/Hamburg/Bremen', 'Nordrhein-Westfalen',
               'Rheinland-Pfalz', 'Schleswig-Holstein', 'Saarland', 'Sachsen',
               'Sachsen-Anhalt', 'Thueringen/Sachsen-Anhalt', 'Thueringen',
               'Deutschland']

if merge is True:
    skip_rows = 3
    df = merge_files_to_dataframe(txt_files, skip_rows)
    df.to_csv("../data/regional_averages_tm_all.csv")
