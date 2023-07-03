import unittest
from dwd_downloader import * 
import sys, os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..')


class TestDownloader(unittest.TestCase):

    def test_string_list_converter_str(self):
        print("\nTesting String List converter: [1/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)

    def test_string_list_converter_list(self):
        print("\nTesting String List converter: [2/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)

    def test_string_list_converter_int(self):
        print("\nTesting String List converter: [3/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)

        
##################################################################

    def test_input_checker_str(self):
        print("\nTesting Input Checker: [1/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)


    def test_input_checker_list(self):
        print("\nTesting Input Checker: [2/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)


    def test_input_checker_int(self):
        print("\nTesting Input Checker: [3/3]")

        result = []
        # .CheckIfOutputIsCorrect(self, result, [], True)

if __name__ == '__main__':
    unittest.main()