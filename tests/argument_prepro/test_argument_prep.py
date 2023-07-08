import unittest
from unittest.mock import patch, Mock
import os
import sys
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.argument_preprocessing import arg_test_year, check_if_year 
from src.argument_preprocessing import arg_test_month, check_if_month
from src.utilities import yaml_reader

class TestArg(unittest.TestCase):
    def test_arg_test_year(self):
        # Create a mock object for args
        args = Mock()
        args.year = ['2000..2005', '2007', '2009']

        # Call the function with the mock args
        arg_test_year(args)

        # Check the result
        self.assertEqual(args.year, [2000, 2001, 2002, 2003, 2004, 2005, 2007, 2009])

    def test_check_if_year(self):
        # Test with a valid year
        year = '2000'
        self.assertIsNone(check_if_year(year))  # check_if_year should not raise an exception

        # Test with an invalid year
        year = 'not a year'
        with self.assertRaises(AssertionError):
            check_if_year(year)  # check_if_year should raise an AssertionError

    @patch('src.utilities.yaml_reader')
    def test_arg_test_month(self, mock_yaml_reader):
        # Mock the yaml_reader function to return a list of month names
        mock_yaml_reader.return_value = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

        # Create a mock object for args
        args = Mock()
        args.month = ['Janua..March', 'May', 'July']

        # Call the function with the mock args
        arg_test_month(args)

        # Check the result
        self.assertEqual(args.month, ['january', 'february', 'march', 'may', 'july'])    

   
if __name__ == '__main__':
    unittest.main()

