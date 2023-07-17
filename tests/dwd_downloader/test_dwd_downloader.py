import unittest
import sys
import os
from unittest.mock import patch, MagicMock

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.dwd_downloader import dwd_downloader
from src.dwd_downloader import input_checker
from src.dwd_downloader import url_checker_handler
from src.dwd_downloader import data_writer


class TestDwdDownloader(unittest.TestCase):

    @patch('src.dwd_downloader.requests.get')
    @patch('src.dwd_downloader.data_writer')
    def test_single_url(self, mock_data_writer, mock_get):
        print("\n Testing DWD Downloader - single URL [1/3]")
        # Test that the function can handle a single URL
        url = str('https://opendata.dwd.de/climate_environment/CDC'
                  '/regional_averages_DE/annual/air_temperature_mean/'
                  'regional_averages_tm_year.txt')
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Test content'
        dwd_downloader(url)
        # Check that data_writer was called with the correct arguments
        mock_data_writer.assert_called_with(f'{parent_dir}/'
                                            'data/annual/air_temperature_mean/'
                                            'regional_averages_tm_year.txt',
                                            'Test content')

    @patch('src.dwd_downloader.requests.get')
    @patch('src.dwd_downloader.data_writer')
    def test_list_of_urls(self, mock_data_writer, mock_get):
        print("\n Testing DWD Downloader - URL list [2/3]")
        urls = ['https://opendata.dwd.de/climate_environment/CDC/'
                'regional_averages_DE/annual/air_temperature_mean/'
                'regional_averages_tm_year.txt',
                'https://opendata.dwd.de/climate_environment/CDC/'
                'regional_averages_DE/annual/precipitation/'
                'regional_averages_rr_year.txt',
                'https://opendata.dwd.de/climate_environment/CDC/'
                'regional_averages_DE/annual/sunshine_duration/'
                'regional_averages_sd_year.txt']

        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Test content'
        dwd_downloader(urls)
        assert mock_data_writer.call_count == 3

    @patch('src.dwd_downloader.requests.get')
    @patch('src.dwd_downloader.data_writer')
    def test_invalid_url(self, mock_data_writer, mock_get):
        print("\n Testing DWD Downloader - Invalid URL [3/3]")
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception):
            dwd_downloader("invalid url")


if __name__ == '__main__':
    unittest.main()
