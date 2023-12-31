import unittest
import os
import sys
from raindeer.user_stories import simple_plot

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")


class TestSimplePlot(unittest.TestCase):
    def test_simple_plot1(self):
        print("Testing simple_plot function [1/1]")
        command = (
                   'python raindeer/main.py precipitation -m january'
                   ' --outfile "results/user_stories/plots/'
                   'simple_plot_temp.png"'
                   ' --mode=simple-plot -y 1981..2022 -b "brandenburg" '
                   '"hessen" -w "precipitation" "sun"')
        os.system(command)
        self.assertTrue(os.path.isfile(
            r"results/user_stories/plots/simple_plot_temp.png"))
        os.remove(r"results/user_stories/plots/simple_plot_temp.png")


if __name__ == '__main__':
    unittest.main()
