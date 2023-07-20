import unittest
from pathlib import Path
import logging
from io import StringIO

from raindeer.dwd_downloader import data_writer


class TestDataWriter(unittest.TestCase):
    def setUp(self):
        # Configure logging to capture the messages
        self.log_stream = StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.INFO)

    def tearDown(self):
        # Reset logging configuration after each test method
        logging.getLogger().handlers.clear()
        logging.getLogger().removeHandler(logging.StreamHandler())

    def test_data_writer(self):
        print("Testing DWD Downloader - Data Writer [1/1]")
        # Define test input
        path = "google.com"
        content = "test"

        # Call the function under test
        data_writer(path, content)

        # Verify the output
        output_file = open(path, "r")
        self.assertEqual(output_file.read(), content)
        output_file.close()

        # Verify the logging message
        log_message = self.log_stream.getvalue().strip()
        print("Logged message:", log_message)
        expected_message = f"Downloaded '{path}' STATUS OK."
        self.assertNotEqual(log_message, expected_message)


if __name__ == '__main__':
    unittest.main()
