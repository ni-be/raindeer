import unittest
import subprocess
from main import main
from unittest.mock import patch, Mock
import argparse


class CLITestCase(unittest.TestCase):
    def test_forecast_mode(self):
        print("Testing CLI main.py - Forecast [1/7]")
        command = [
            'python', 'raindeer/main.py',
            'data/annual/air_temperature_mean/air_temperature_mean_year.txt',
            '--mode=forecast', '-b=Deutschland']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 0)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  '
        'data/annual/air_temperature_mean/air_temperature_mean_year.txt'
        self.assertEqual(first_line, expected_first_line)

    def test_plot_params_mode(self):
        print("Testing CLI main.py - Plot Parameter [2/7]")
        command = ['python', 'raindeer/main.py', 'data/annual',
                   '--mode=plot_param', '-b="Baden-Wuertemberg"']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 1)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  data/annual'
        self.assertEqual(first_line, expected_first_line)

    def test_fourier_mode(self):
        print("Testing CLI main.py - Fourier [3/7]")
        command = ['python', 'raindeer/main.py', 'precipitation',
                   '--mode=fourier', '-b="Hessen" "Deutschland"']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 1)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  precipitation'
        self.assertEqual(first_line, expected_first_line)

    def test_plot_between_years(self):
        print("Testing CLI main.py - Between years [4/7]")
        command = ['python', 'raindeer/main.py',
                   'precipitation', '--mode=fourier',
                   '-b="Deutschland"' '-w=precipitation', '-y=2000..2001']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 1)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  precipitation'
        self.assertEqual(first_line, expected_first_line)

    def test_dataframe_helper_mode(self):
        print("Testing CLI main.py - DF helper [5/7]")
        command = ['python', 'raindeer/main.py', '-dt=precipitation',
                   '-i=annual', '-m=january', '--mode=dataframe_helper']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 2)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = ''
        self.assertEqual(first_line, expected_first_line)

    def test_plot_between_years(self):
        print("Testing CLI main.py - Simple Plot [6/7]")
        command = ['python', 'raindeer/main.py', '"data/annual"',
                   '--mode=simple-plot', '-y=2000', '-m=january',
                   '-b="Brandenburg"', '-w="precipitation"']
        result = subprocess.run(command, capture_output=True, text=True)
        # Ensure the command executed successfully
        self.assertEqual(result.returncode, 1)
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = "data/annual"
        self.assertNotEqual(first_line, expected_first_line)

    def test_invalid(self):
        print("Testing CLI, test invalid [7/7]")
        command = ['python', 'raindeer/main.py', '--mode=wrong']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
