# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 12:42:22 2023

@author: timow
"""

import pytest
import fourier
import between_years
import pandas as pd

df = pd.read_csv('../data/monthly/precipitation/regional_averages_tm_all.csv')


def test_fourier_input_table():
    "Test for fourier analysis implementation for weather data"

    with pytest.raises(AssertionError):
        fourier.fourier_analysis(df, 'Deutschland', 'rain')


def test_between_years():
    "Test plot_between_years for behavior if non valid dates are given"

    with pytest.raises(TypeError):
        between_years.plot_between_years(df, [177001, 'a'],
                                         'Deutschland', 'rain')