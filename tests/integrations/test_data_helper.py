import unittest
from raindeer.data_helper import data_helper


class TestDataHelper(unittest.TestCase):

    def setUp(self):
        # A valid DWD data to be tested
        self.dwd_data_valid = ["precipitation"]
        # A valid interval to be tested
        self.interval_valid = ["annual", "monthly"]
        # A valid option to be tested
        self.option_valid = "w"

        self.dwd_data_invalid = 123  # An invalid DWD data to be tested
        self.interval_invalid = "yearly"  # An invalid interval to be tested
        self.option_invalid = "z"  # An invalid option to be tested

    def test_data_helper_valid(self):
        print("Testing Data_helper integretity valid input [1/2]")
        # Test the function with a valid set of arguments
        result = data_helper(
            self.dwd_data_valid, self.interval_valid, self.option_valid)
        self.assertIsInstance(result, list)

    def test_data_helper_invalid(self):
        print("Testing Data_helper integretity - invalid input[2/2]")
        # Test the function with invalid inputs
        with self.assertRaises(AssertionError):
            data_helper(
                self.dwd_data_invalid, self.interval_valid, self.option_valid)

        with self.assertRaises(AssertionError):
            data_helper(
                self.dwd_data_valid, self.interval_invalid, self.option_valid)

        with self.assertRaises(AssertionError):
            data_helper(
                self.dwd_data_valid, self.interval_valid, self.option_invalid)


if __name__ == '__main__':
    unittest.main()
