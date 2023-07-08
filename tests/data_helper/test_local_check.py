import unittest
import sys
import os
from unittest import mock
root_dir = os.path.dirname(os.path.abspath(__file__)) 
parent_dir = os.path.dirname(os.path.dirname(root_dir))

sys.path.append(f"{parent_dir}/src")

from src.data_helper import local_check 


class TestLocalCheck(unittest.TestCase):
    def setUp(self):
        self.directory = ['/data/annual/precipitation', '/data/annual/temperature']
        self.download_url_list = ['url1', 'url2']

    @mock.patch('os.path.exists')
    @mock.patch('src.data_helper.create_url_download_list')
    def test_local_check_nonexistent_path(self, mock_create_url_download_list, mock_exists):
        print("\n Testing Local Check Test: nonexistent path  [1/2]")

        mock_exists.side_effect = lambda path: path not in self.directory
        mock_create_url_download_list.return_value = self.download_url_list

        result = local_check(self.directory)

        mock_create_url_download_list.assert_called_once_with(self.directory)
        mock_exists.assert_has_calls([mock.call(path) for path in self.directory])
        self.assertEqual(result, self.download_url_list)

    @mock.patch('os.path.exists')
    @mock.patch('src.data_helper.create_url_download_list')
    def test_local_check_existing_path(self, mock_create_url_download_list, mock_exists):
        print("\n Testing Local Check Test: exisiting path [2/2]")

        mock_exists.side_effect = lambda path: path in self.directory
        mock_create_url_download_list.return_value = []

        result = local_check(self.directory)

        mock_create_url_download_list.assert_called_once_with([])
        mock_exists.assert_has_calls([mock.call(path) for path in self.directory])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
