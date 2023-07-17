import unittest
from your_module import dataframe_helper
from pandas.util.testing import assert_frame_equal
import pandas as pd

class Testdataframe_helper(unittest.TestCase):
    """
    Define a class in which the tests will run
    """

    def test_dataframe_helper_type_exceptions(self):
        """
        Test exceptions related to input types
        """
        with self.assertRaises(TypeError): 
            dataframe_helper(123, 'monthly', '01', 'w') 
            # check if raises TypeError for wrong data
        with self.assertRaises(TypeError): 
            dataframe_helper('air_temperature_mean', 123, '01', 'w') 
            # check if raises TypeError for wrong interval
        with self.assertRaises(TypeError): 
            dataframe_helper('air_temperature_mean', 'monthly', {}, 'w') 
            # check if raises TypeError for wrong month_range
        with self.assertRaises(TypeError): 
            dataframe_helper('air_temperature_mean', 'monthly', '01', 123) 
            # check if raises TypeError for wrong option

    def test_dataframe_helper_value_exceptions(self):
        """
        Test exceptions related to input values
        """
        with self.assertRaises(ValueError): 
            dataframe_helper('unknown_value', 'monthly', '01', 'w') 
            # check if raises ValueError for wrong data value
        with self.assertRaises(ValueError): 
            dataframe_helper('air_temperature_mean', 'unknown_value', '01', 'w') 
    # check if raises ValueError for wrong interval value

    def test_dataframe_helper_valid_inputs(self):
        """
        Test normal behavior with valid inputs
        """
        # define your test data
        data = ['air_temperature_mean', 'frost_days']
        interval = ['monthly', 'annual']
        month_range = ['01', '02', '03']
        option = 'w'

        # call the function with the test data
        result = dataframe_helper(data, interval, month_range, option)

        # define your expected output
        # Please change this according to function implementation and 
        # correct expected output
        expected_output = [...]  # fill this with the expected output

        # assert that the result is as expected, row by row
        for result_df, expected_df in zip(result, expected_output):
            assert_frame_equal(result_df, expected_df)

if __name__ == '__main__':
    unittest.main()