import unittest
import io
from unittest.mock import mock_open, patch
from raindeer.utilities import yaml_reader

class YamlReaderTestCase(unittest.TestCase):
    def test_value_error(self):
        print("Testing Yaml Reader Value Error [1/1]")
        with patch('builtins.open', mock_open()) as mock_file:
            # Create a mock file-like object using io.StringIO
            file_content = """
            option1: value1
            option2: value2
            """
            mock_file.return_value.__enter__.return_value = io.StringIO(file_content)
            
            with self.assertRaises(ValueError):
                yaml_reader('invalid_option')

if __name__ == '__main__':
    unittest.main()