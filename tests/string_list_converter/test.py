import unittest
import sys, os
# insert at 1, 0 is the script path (or '' in REPL)
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.dwd_downloader import string_list_converter  

class TestStringListConverter(unittest.TestCase):
    def test_string_list_converter(self):
        # Test that the function correctly converts string to list
        self.assertEqual(string_list_converter("test"), ['test'])  

  
if __name__ == '__main__':
    unittest.main()
