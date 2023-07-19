import unittest
import subprocess

class CLITestCase(unittest.TestCase):
    def test_forecast_mode(self):
        print("Testing CLI main.py - Forecast [1/7]")
        command = ['python', 'raindeer/main.py', 'data/annual/air_temperature_mean/air_temperature_mean_year.txt',
                   '--mode=forecast', '-b=Deutschland']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)  # Ensure the command executed successfully
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  data/annual/air_temperature_mean/air_temperature_mean_year.txt'
        self.assertEqual(first_line, expected_first_line)        

    def test_plot_params_mode(self):
        print("Testing CLI main.py - Plot Parameter [2/7]")
        command = ['python', 'raindeer/main.py', 'data/annual','--mode=plot_param', '-b="Baden-Wuertemberg"']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)  # Ensure the command executed successfully
        # Add assertions for the expected output or behavior
        # Additional assertions for DataFrame output
        first_line = result.stdout.strip().split('\n')[0]
        expected_first_line = 'inputfile:  data/annual'
        self.assertEqual(first_line, expected_first_line)     
               
if __name__ == '__main__':
    unittest.main()
