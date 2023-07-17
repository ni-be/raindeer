import unittest
from unittest.mock import patch
import os
import sys
from raindeer.user_stories import fourier_analysis

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")


class TestFourierAnalysis(unittest.TestCase):
    @patch("matplotlib.pyplot.show")
    def test_fourier_analysis(self, mock_show):
        print("\n Testing Fourier Analysis [1/1]")
        fourier_analysis('precipitation', 'annual',
                         ['bayern', 'hessen'], 'sun')


if __name__ == '__main__':
    unittest.main()
