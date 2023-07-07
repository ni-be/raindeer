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
        self.ending = 'test'

    def test_write_csv(self):
        # Call the function
        write_csv(self.df, self.ending)

        # Check if the file was created
        self.assertTrue(os.path.isfile(f"{parent_dir}/{self.ending}_combined_data.csv"))

        # Load the file and compare with the original dataframe
        df_loaded = pd.read_csv(f"{parent_dir}/{self.ending}_combined_data.csv")
        pd.testing.assert_frame_equal(self.df, df_loaded)

    def tearDown(self):
        # Remove the created file
        os.remove(f"{parent_dir}/{self.ending}_combined_data.csv")

if __name__ == '__main__':
    unittest.main()
