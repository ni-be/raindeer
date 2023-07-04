"""Processes and visualizes different data
relating to the climate"""

import argparse
# from data_helper import *
import pandas as pd
from typing import List
import argument_preprocessing as argpre


def main(data):
    argpre.arg_preprocess(args)

    if args.mode == "PLACEHOLDER1":
        # use case function here
        pass
    elif args.mode == "PLACEHOLDER2":
        # another use case function here
        pass
    else:
        print(str(args.mode)+" is not a valid mode")


# CLI entry point
# more optons should be added here later.
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', help='file to process',
                        type=str, nargs="?")
    parser.add_argument('--url', help='url to process',
                        type=str, nargs="?")
    parser.add_argument('--outfile', help='location to save file',
                        type=str, nargs="?")
    parser.add_argument('--mode', help='process mode',
                        type=str, nargs="?", default="simpleplot")
    parser.add_argument('--year', '-y', help='timeframe in years',
                        type=str, nargs="+", default=["2000..2020"])
    parser.add_argument('--month', '-m', help='timeframe in months',
                        type=str, nargs="+", default=None)
    parser.add_argument('--bundesland', '-b', '-land', help="""bundesland
                        to analyse""",
                        type=str, nargs="+", default=None)
    parser.add_argument('--weather', '-w', help="""weather phenomenom
                        to analyse""",
                        type=str, nargs="+", default=["precipitation"])

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
