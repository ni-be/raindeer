"""
USER STORY TESTS: 3, 8

"""
import unittest
import os
import sys
import numpy as np

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.user_stories import linear_regression
from src.user_stories import predict_temperature_next_year


class TestUserStory8(unittest.TestCase):

    def test_linear_regression_one(self):
        print("\n Testing user story 8 [1/2]")
        x_data = np.asarray([2, 3, 4])
        y_data = np.asarray([7, 9, 11])
        result = linear_regression(x_data, y_data, 7)
        self.assertEqual(result, 17.0)

    def test_linear_regression_two(self):
        print("\n Testing user story 8 [2/2]")
        x_data = np.empty(2)
        y_data = np.empty(3)
        with self.assertRaises(AssertionError):
            linear_regression(x_data, y_data, 1)

    def test_predict_temperature_next_year(self):
        self.assertAlmostEqual(10.0, predict_temperature_next_year(), places=5)


if __name__ == '__main__':
    unittest.main()
