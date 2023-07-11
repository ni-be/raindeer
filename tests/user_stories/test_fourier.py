import pandas as pd
import unittest
import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/src")

from src.user_stories import fourier_analysis


class TestFourierAnalysis(unittest.TestCase):
    def test_fourier_input_table(self):
        "Test for fourier analysis implementation for weather data"
        with self.assertRaises(AssertionError):
            fourier_analysis("precipitation", "monthly", 'Deutschland', 'rain')


if __name__ == '__main__':
    unittest.main()
