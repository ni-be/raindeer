import unittest
from raindeer.dwd_downloader import input_checker


class TestInputChecker(unittest.TestCase):
    def test_else_branch(self):
        print("Testing Input Checker: [1/1]")
        self.assertEqual(input_checker(123), ['123'])  
    # The input is neither a string nor a list

if __name__ == '__main__':
    unittest.main()