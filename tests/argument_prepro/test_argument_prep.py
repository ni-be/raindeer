import unittest
from unittest.mock import patch, Mock
from unittest.mock import MagicMock
import os
import sys
root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

# BECAUSE RUNNING IN DIFFERENT PATH,... EVEN IF PYCODESTYLE DOES NOT LIKE IT
# LEAVE IT AS IT IS!
from src.argument_preprocessing import arg_test_year, check_if_year
from src.argument_preprocessing import arg_test_month, check_if_month
from src.utilities import yaml_reader
from src.argument_preprocessing import arg_test_weather
from src.argument_preprocessing import arg_test_bundesland


class TestArg(unittest.TestCase):
    def test_arg_test_year(self):
        print("\n Testing Argument Tests - arg_test_year  [1/5]")
        # Create a mock object for args
        args = Mock()
        args.year = ['2000..2005', '2007', '2009']

        # Call the function with the mock args
        arg_test_year(args)

        # Check the result
        self.assertEqual(args.year,
                         [2000, 2001, 2002, 2003, 2004, 2005, 2007, 2009])

    def test_check_if_year(self):
        print("\n Testing Argument Tests - test check year [2/5]")
        # Test with a valid year
        year = '2000'
        self.assertIsNone(check_if_year(year))
        # check_if_year should not raise an exception

        # Test with an invalid year
        year = 'not a year'
        with self.assertRaises(AssertionError):
            check_if_year(year)
        # check_if_year should raise an AssertionError

    @patch('src.utilities.yaml_reader')
    def test_arg_test_month(self, mock_yaml_reader):
        print("\n Testing Argument Tests - arg_test_month [3/5]")

        # Mock the yaml_reader function to return a list of month names
        mock_yaml_reader.return_value = ['january', 'february', 'march',
                                         'april', 'may', 'june', 'july',
                                         'august', 'september', 'october',
                                         'november', 'december']

        # Create a mock object for args
        args = Mock()
        args.month = ['January..March', 'May', 'July']
        # Call the function with the mock args
        arg_test_month(args)

        # Check the result
        self.assertEqual(args.month, ['january', 'february', 'march',
                                      'may', 'july'])

    @patch('src.utilities.yaml_reader')
    def test_arg_test_weather(self, mock_yaml_reader):
        print("\n Testing Argument Tests arg_test_weather [4/5]")

        # Mock the yaml_reader function to return weather options
        mock_yaml_reader.return_value = ['air_temperature_mean',
                                         'precipitation', 'sunshine_duration']

        # Create a mock object for args
        args = Mock()
        args.weather = ['air_temperature_mean', 'precipitation',
                        'sunshine_duration']

        # Call the function with the mock args
        arg_test_weather(args)

        # Check the result
        self.assertEqual(args.weather, ['air_temperature_mean',
                                        'precipitation', 'sunshine_duration'])

        # Check if the yaml_reader function was called with the correct arg
        # mock_yaml_reader.assert_called_once_with('monthly_data_type')

    def test_arg_test_bundesland(self):
        print("\n Testing Argument Tests arg_test_bundesland [5/5]")
        # Mock the args object
        args = MagicMock()
        args.bundesland = ["Berlin", "Hamburg", "all"]

        # Mock the yaml_reader function
        def yaml_reader(filename):
            return ["Jahr;Monat", "brandenburg/berlin", "brandenburg",
                    "baden-wuerttemberg", "bayern", "hessen",
                    "mecklenburg-vorpommern", "niedersachsen",
                    "niedersachsen/hamburg/bremen", "nordrhein-westfalen",
                    "rheinland-pfalz", "schleswig-holstein", "saarland",
                    "sachsen", "sachsen-anhalt",
                    "thueringen/sachsen-anhalt", "thueringen", "deutschland"]

        # Mock the check_if_bundesland function
        def check_if_bundesland(bundesland, bundesland_options):
            pass

        # Assign the mocked functions to the original functions
        original_yaml_reader = yaml_reader
        original_check_if_bundesland = check_if_bundesland

        try:
            # Replace the original functions with the mocked ones
            globals()["yaml_reader"] = yaml_reader
            globals()["check_if_bundesland"] = check_if_bundesland

            # Call the function to be tested
            arg_test_bundesland(args)

            # Assert the expected output
            expected_output = ["Jahr;Monat", "brandenburg/berlin",
                               "brandenburg", "baden-wuerttemberg",
                               "bayern", "hessen", "mecklenburg-vorpommern",
                               "niedersachsen",
                               "niedersachsen/hamburg/bremen",
                               "nordrhein-westfalen", "rheinland-pfalz",
                               "schleswig-holstein", "saarland", "sachsen",
                               "sachsen-anhalt", "thueringen/sachsen-anhalt",
                               "thueringen"]

            self.assertEqual(args.bundesland, expected_output)
        finally:
            # Restore the original functions
            globals()["yaml_reader"] = original_yaml_reader
            globals()["check_if_bundesland"] = original_check_if_bundesland


if __name__ == '__main__':
    unittest.main()
