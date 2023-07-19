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
        print("Testing Rename Function - not matching [1/4]")
        #print("Logged message:", log_message)
        filename = "non_existing_file.doc"
        with self.assertRaises(ValueError):
            rename_function(filename, self.data_type, self.ending, self.path)


    def test_data_type_not_string(self):
        print("Testing Rename Function - not String [2/4]")
        filename = "existing_file.txt"
        data_type = {}
        with self.assertRaises(TypeError):
            rename_function(filename, data_type, self.ending, self.path)


    def test_path_not_list(self):
        print("Testing Rename Function - path not a list [3/4]")
        filename = "existing_file.txt"
        path = {}
        with self.assertRaises(TypeError):
            rename_function(filename, self.data_type, self.ending, path)
   
    def test_rename_function(self):
        print("Testing Rename Function - multiple inputs [4/4]")
        filename = "example.txt"
        path = self.path

        # Test that the function raises the correct exceptions
        with self.assertRaises(TypeError):
            rename_function(filename, None, self.ending, path)
            rename_function(filename, self.data_type, int(0), path)
            rename_function(filename, self.data_type, self.ending, None)

        with self.assertRaises(ValueError):
            rename_function("example.doc", self.data_type, self.ending, path)
    
    
if __name__ == '__main__':
    unittest.main()