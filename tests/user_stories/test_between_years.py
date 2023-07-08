# -*- coding: utf-8 -*-

import pandas as pd
import unittest
import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.between_years import plot_between_years


class TestPlotBetweenYears(unittest.TestCase):
    def test_between_years(self):
        "Test plot_between_years for behavior if non valid dates are given"
        with self.assertRaises(TypeError):
            plot_between_years("precipitation", "monthly", [177001, 'a'], 'Deutschland', 'rain')



if __name__ == '__main__':
    unittest.main()
