import unittest
import sys
import os
from unittest.mock import patch, MagicMock

root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.dwd_downloader import dwd_downloader

class TestDWDdownloader(unittest.TestCase):
    def setUp(self):
        self.url_list = ["https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt", "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/annual/air_temperature_mean/regional_averages_tm_year.txt"]
           
    @patch('src.dwd_downloader.input_checker')
    @patch('src.dwd_downloader.url_checker_handler')
    def test_dwd_downloader(self, mock_input_checker, mock_url_checker_handler):
    # Mock the behavior of input_checker and url_checker_handler functions
        mock_input_checker.return_value = self.url_list
        
        mock_url_checker_handler.return_value = None  # The function does not have a return value
   
        # Call the function with the test data
        dwd_downloader(self.url_list)
   
        # Assert expected behavior
        self.assertEqual(mock_input_checker.call_count, 2)
        mock_url_checker_handler.assert_called_once()

if __name__ == '__main__':
    unittest.main()
