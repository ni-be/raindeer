import unittest
from unittest.mock import patch
import sys
import os
from raindeer.data_helper import create_url_download_list

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")

class TestURLDownloadList(unittest.TestCase):

    @patch('raindeer.utilities.yaml_reader')
    def test_create_url_download_list(self, mock_yaml_reader):
        print("Testing Create URL download list - valid  [1/4]")

        # define the mock behavior of yaml_reader
        mock_yaml_reader.return_value = ['https://opendata.dwd.de/'
                                         'climate_environment/CDC/'
                                         'regional_averages_DE/annual/'
                                         'precipitation/'
                                         'regional_averages_rr_year.txt']
        # call the function with test input
        test_input = ['/data/annual/precipitation']
        result = create_url_download_list(test_input)

        # check the output
        expected_output = ['https://opendata.dwd.de/climate_environment/CDC'
                           '/regional_averages_DE/annual/precipitation/'
                           'regional_averages_rr_year.txt',
                           'https://opendata.dwd.de/climate_environment/CDC/'
                           'regional_averages_DE/monthly/'
                           'precipitation/regional_averages_rr_{}.txt']
        self.assertEqual(result, expected_output)

    @patch('raindeer.utilities.yaml_reader')
    def test_not_list(self, mock_yaml_reader):
        print("Testing Create URL download list - not list [2/4]")
        # define the mock behavior of yaml_reader
        mock_yaml_reader.return_value = {'https://opendata.dwd.de/'
                                         'climate_environment/CDC/'
                                         'regional_averages_DE/annual/'
                                         'precipitation'}
        with self.assertRaises(TypeError):
            create_url_download_list(int(8))

    @patch('raindeer.utilities.yaml_reader')
    def test_element_not_str(self, mock_yaml_reader):
        print("Testing Create URL download list - Url not str [3/4]")
        # define the mock behavior of yaml_reader
        mock_yaml_reader.return_value = ['https://opendata.dwd.de/'
                                         'climate_environment/CDC/'
                                         'regional_averages_DE/annual/'
                                         'precipitation']
        with self.assertRaises(TypeError):
            create_url_download_list([1, 2, 3])

    @patch('raindeer.utilities.yaml_reader')  
    def test_yaml_not_list(self, mock_yaml_reader):
        print("Testing Create URL download list - yaml reader [4/4]")
        # define the mock behavior of yaml_reader
        mock_yaml_reader.return_value = "abc"
        with self.assertRaises(TypeError):
            create_url_download_list({1:"abc"})


if __name__ == '__main__':
    unittest.main()
