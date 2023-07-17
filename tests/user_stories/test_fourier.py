import pandas as pd
import unittest
from unittest.mock import patch
import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")

from raindeer.user_stories import fourier_analysis


class TestFourierAnalysis(unittest.TestCase):
    def test_fourier_input_table(self):
        print("\n Testing Fourier Analysis [1/2]")
        "Test for fourier analysis implementation for weather data"
        with self.assertRaises(AssertionError):
            fourier_analysis("precipitation", "monthly", 'Deutschland', 'rain')

    @patch("matplotlib.pyplot.show")
    def test_fourier_analysis(self, mock_show):
        print("\n Testing Fourier Analysis [1/2]")
        fourier_analysis('precipitation', 'annual',
                         ['bayern', 'hessen'], 'sun')



if __name__ == '__main__':
    unittest.main()
