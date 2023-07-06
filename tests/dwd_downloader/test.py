import unittest
import os
from src.dwd_downloader import dwd_downloader
from unittest.mock import patch

class TestDownloader(unittest.TestCase):
    @patch('src.global_var', "/annual/precipation/precipation_yearly.txt")

    def test_single_url(self):
        
        url = "http://example.com"
        result = dwd_downloader(url)
        self.assertIsInstance(result, list, "Result should be a list")
        # Check if file exists in output directory
        for file_name in result:
            with self.subTest(file_name=file_name):
                self.assertTrue(os.path.isfile(file_name))

    def test_multiple_urls(self):
        urls = ["http://example.com", "http://example2.com"]
        result = dwd_downloader(urls)
        self.assertIsInstance(result, list, "Result should be a list")
        # Check if file exists in output directory
        for file_name in result:
            with self.subTest(file_name=file_name):
                self.assertTrue(os.path.isfile(file_name))
    
    def test_invalid_input(self):
        non_string = 1234
        with self.assertRaises(TypeError):
            dwd_downloader(non_string)
        non_list = {"key": "value"}
        with self.assertRaises(TypeError):
            dwd_downloader(non_list)


#@patch('main.global_var', "Mocked Value")
#        def test_global_var(self):
#            self.assertEqual(main.global_var, "Mocked Value")

if __name__ == '__main__':
    unittest.main()
