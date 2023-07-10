import unittest
import sys
import os
from unittest.mock import patch
root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.data_helper import create_url_download_list


class TestURLDownloadList(unittest.TestCase):

    @patch('src.utilities.yaml_reader')
    def test_create_url_download_list(self, mock_yaml_reader):
        print("\n Testing Create URL download list [1/1]")

        # define the mock behavior of yaml_reader
        mock_yaml_reader.return_value = ['https://opendata.dwd.de/\
        climate_environment/CDC/regional_averages_DE/annual/precipitation\
        /regional_averages_rr_year.txt']

        # call the function with test input
        test_input = ['/data/annual/precipitation']
        result = create_url_download_list(test_input)

        # check the output
        expected_output = ['https://opendata.dwd.de/climate_environment/CDC\
            /regional_averages_DE/annual/precipitation/\
            regional_averages_rr_year.txt', 'https://opendata.dwd.de/\
            climate_environment/CDC/regional_averages_DE/monthly/\
            precipitation/regional_averages_rr_{}.txt']
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
