import unittest
from unittest.mock import patch, mock_open
import os
import sys
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.data_helper import txt_renamer 

class TestTxtRenamer(unittest.TestCase):
    @patch('os.listdir')
    @patch('src.data_helper.rename_function')  
    def test_txt_renamer(self, mock_rename_function, mock_listdir):
        # Mock the os.listdir function to return a list of filenames
        mock_listdir.return_value = ['precipitation.txt', 'precipiation.csv', 'file3.txt']

        # Call the function with a test path
        path = [f"{parent_dir}/data/monthly/precipitation", f"{parent_dir}/data/annual/precipitation"]
        txt_renamer(path)

        # Check if rename_function was called the expected number of times
        self.assertEqual(mock_rename_function.call_count, 6)

        # Check the arguments of the first call to rename_function
        first_call_args = mock_rename_function.call_args_list[0]
        self.assertEqual(first_call_args[0][0], 'precipitation.txt')  # filename
        self.assertEqual(first_call_args[0][1], 'precipitation')  # data_type
        self.assertEqual(first_call_args[0][2], 'ion.txt')  # ending
        self.assertEqual(first_call_args[0][3], f"{parent_dir}/data/monthly/precipitation")

if __name__ == '__main__':
    unittest.main()

