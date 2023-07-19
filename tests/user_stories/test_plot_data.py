import unittest
from unittest.mock import patch
from raindeer.user_stories import plot_data


class TestPlotData(unittest.TestCase):

    @patch("matplotlib.pyplot.show")
    def test_plot_data(self, mock_show):
        print("Testing Plot Data [1/1]")
        plot_data([1,2,3], [2,4,6], 'title', 'x', 'y')


if __name__ == '__main__':
    unittest.main()
