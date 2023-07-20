import unittest
from unittest.mock import patch, Mock
from raindeer.dwd_downloader import url_checker_handler
from raindeer.dwd_downloader import data_writer
import urllib.request
import urllib.response


class UrlCheckerHandlerTestCase(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_invalid_url(self, mock_urlopen):
        print("Testing URL Checker - Invalid URL [1/1]")
        mock_urlopen.return_value = Mock(spec=urllib.response.addinfourl)
        mock_urlopen.return_value.status = 404

        path = "/path/to/file.txt"
        url = "http://example.com/file.txt"

        with patch(
            'raindeer.dwd_downloader.logging.error'
                ) as mock_logging_error:
            url_checker_handler(path, url)

            mock_logging_error.assert_called_once_with(
                "Error downloading file: file.txt.")


if __name__ == '__main__':
    unittest.main()
