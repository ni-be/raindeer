"""Processes and visualizes different data
relating to the climate"""

import argparse
# from data_helper import *
import pandas as pd
from typing import List
import argument_preprocessing as argpre
import user_stories
import utilities as utils


def main(data):
    argpre.arg_preprocess(args)

    if args.mode == "forecast":
        # Works with the following command: python src/raindeer.py
        # "data/annual/air_temperature_mean/regional_averages_tm_year.txt"
        # --mode=forecast -b='Deutschland'
        time = args.year
        place = args.bundesland[0].title()
        means = utils.load_dataset(data).loc[time, place].to_numpy()
        print(user_stories.linear_regression(time, means, args.forecast,
                                             'Time in years',
                                             'Temperature mean in °C'))
    elif args.mode == "plot-params":
        # Works with the following command: python src/raindeer.py
        # "data/annual" --mode=plot-params -b='Baden-Wuerttemberg'
        time = args.year
        place = args.bundesland[0].title()
        user_stories.plot_weather_parameters_annual(time, place, data)
    elif args.mode == "PLACEHOLDER":
        pass
    else:
        print(str(args.mode) + " is not a valid mode")


# CLI entry point
# more options should be added here later.
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', help='file to process',
                        type=str, nargs="?")
    parser.add_argument('--url', help='url to process',
                        type=str, nargs="?")
    parser.add_argument('--outfile', help='location to save file',
                        type=str, nargs="?")
    parser.add_argument('--mode', help='process mode',
                        type=str, nargs="?", default="simple-plot")
    parser.add_argument('--year', '-y', help='timeframe in years',
                        type=str, nargs="+", default=["2000..2020"])
    parser.add_argument('--month', '-m', help='timeframe in months',
                        type=str, nargs="+", default=None)
    parser.add_argument('--bundesland', '-b', '-land', help="""bundesland
                        to analyse""",
                        type=str, nargs="+", default=None)
    parser.add_argument('--weather', '-w', help="""weather phenomenon
                        to analyse""",
                        type=str, nargs="+", default=["precipitation"])
    parser.add_argument('--forecast', '-f', help="""Time to make forecast 
                        for""", type=int, nargs="?", default=2023)

    args = parser.parse_args()
    if args.url:
        print("input url: ", args.url)
        main(args.url)

    elif args.infile:
        print("inputfile: ", args.infile)
        main(args.infile)

    else:
        print("No url or file provided")
        parser.print_help()
