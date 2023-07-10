"""
USER STORY TESTS: 3

"""
import unittest
import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.user_stories import plot_weather_parameters_annual


class TestUserStory3(unittest.TestCase):
    def test_plot_weather_parameters_annual_one(self):
        print("\n Testing user story 3 [1/2]")
        with self.assertRaises(AssertionError):
            plot_weather_parameters_annual([1923, 1925, 1924])

    def test_plot_weather_parameters_annual_two(self):
        print("\n Testing user story 3 [2/2]")
        # Additional test case with sorted years
        plot_weather_parameters_annual([1981, 1982, 1983])


if __name__ == '__main__':
    unittest.main()
