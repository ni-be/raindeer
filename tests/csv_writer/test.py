import unittest
import sys
import os
import pandas as pd
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.dataframe_helper import write_csv 

class TestWriteCsv(unittest.TestCase):
    def setUp(self):
        # Create a sample dataframe
        self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.data = f"{parent_dir}/data/monthly"  # replace with actual data directory
        self.ending = 'test'

    def test_write_csv(self):
        # Call the function with correct arguments
        write_csv(self.df, self.data, self.ending)

        # Check if the file exists
        self.assertTrue(os.path.isfile(f"{self.data}/{self.ending}_combined_data.csv"))

    def tearDown(self):
        # Check if the file exists before trying to remove it
        if os.path.isfile(f"{self.data}/{self.ending}_combined_data.csv"):
            os.remove(f"{self.data}/{self.ending}_combined_data.csv")

if __name__ == '__main__':
    unittest.main()