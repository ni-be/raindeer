import unittest
import sys
import os
import pandas as pd
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.dataframe_helper import dataframe_creator

class TestDataframeCreator(unittest.TestCase):
    def test_dataframe_creator(self):
        # Test with annual data
        data = f"{parent_dir}/data/annual/precipitation"  # replace with actual path
        df = dataframe_creator(data, 'annual', '00', False)
        self.assertIsInstance(df, pd.DataFrame)

        # Test with monthly data
        data = f"{parent_dir}/data/monthly/precipitation"  # replace with actual path
        df = dataframe_creator(data, 'monthly', ['01', '02'], False)
        self.assertIsInstance(df, pd.DataFrame)

        # Test with invalid interval
        with self.assertRaises(ValueError):
            dataframe_creator(data, 'invalid_interval', 'none', False)

          
if __name__ == '__main__':
    unittest.main()
