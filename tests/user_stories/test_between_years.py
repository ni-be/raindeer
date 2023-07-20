import unittest
from unittest.mock import patch
import os
import sys
from raindeer.user_stories import plot_between_years

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")


class TestPlotBetweenYears(unittest.TestCase):
    def test_between_years(self):
        print("Testing User Story - between years [1/2]")

        # Test plot_between_years for behavior if non-valid dates are given
        with self.assertRaises(TypeError):
            plot_between_years("precipitation", "monthly", [177001, 'a'],
                               'deutschland', 'rain')

    @patch("matplotlib.pyplot.show")
    def test_between_years_simple(self, mock_show):
        print("Testing User Story - between years [2/2]")
        plot_between_years('precipitation', 'monthly', [198101, 202101],
                           'deutschland', 'temp', 'simple')


if __name__ == '__main__':
    unittest.main()
