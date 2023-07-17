import unittest
import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/raindeer")

from raindeer.dwd_downloader import string_list_converter


class TestStringListConverter(unittest.TestCase):
    def test_string_list_converter(self):
        print("\n Testing String list converter: String [1/3]")

        # Test that the function correctly converts string to list
        self.assertEqual(string_list_converter('test'), ['test'])

    def test_integer_input(self):
        print("\n Testing String list converter: Int [2/3]")

        # Test that the function handles integer inputs correctly
        self.assertEqual(string_list_converter(123), ['123'])

    def test_empty_string(self):
        print("\n Testing String list converter: Empty string [3/3]")

        # Test that the function handles empty strings correctly
        self.assertEqual(string_list_converter(''), [''])


if __name__ == '__main__':
    unittest.main()
