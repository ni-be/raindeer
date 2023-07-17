import unittest
import os
import sys
from raindeer.user_stories import simple_plot

root_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(root_dir))
sys.path.append(f"{parent_dir}/raindeer")


class TestSimplePlot(unittest.TestCase):
    def test_simple_plot1(self):
        print("\n Testing simple_plot function")
        os.system(r"python raindeer\raindeer.py data\annual --mode=simple-plot --outfile results/user_stories/plots/simple_plot_temp.png -y 2000..2020 -b Brandenburg thueringen -m January..March -w precipitation")
        self.assertTrue(os.path.isfile(
            r"results/user_stories/plots/simple_plot_temp.png"))
        os.remove(r"results/user_stories/plots/simple_plot_temp.png")

if __name__ == '__main__':
    unittest.main()
