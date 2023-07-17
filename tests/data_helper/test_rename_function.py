import unittest
import os
import sys
from raindeer.data_helper import rename_function  


root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")


class TestRenameFunction(unittest.TestCase):
    def setUp(self):  # Setup method to prepare the envirn.
        self.data_type = "precipitation"
        self.ending = "_year.txt"
        self.path = f"{parent_dir}/data/annual/"  
            
    def test_filename_not_matching(self):
        filename = "non_existing_file.doc"
        with self.assertRaises(ValueError):
            rename_function(filename, self.data_type, self.ending, self.path)


    def test_data_type_not_string(self):
        filename = "existing_file.txt"
        data_type = {}
        with self.assertRaises(TypeError):
            rename_function(filename, data_type, self.ending, self.path)


    def test_path_not_list(self):
        filename = "existing_file.txt"
        path = {}
        with self.assertRaises(TypeError):
            rename_function(filename, self.data_type, self.ending, path)
   
    def test_rename_function(self):
        # Test logic goes here
        filename = "example.txt"
        path = self.path

        # Test that the function raises the correct exceptions
        with self.assertRaises(TypeError):
            rename_function(filename, None, self.ending, path)
            rename_function(filename, self.data_type, None, path)
            rename_function(filename, self.data_type, self.ending, None)

        with self.assertRaises(ValueError):
            rename_function("example.doc", self.data_type, self.ending, path)
    
    
if __name__ == '__main__':
    unittest.main()