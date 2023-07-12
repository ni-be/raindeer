"""Processes and visualizes different data
relating to the climate"""

import argparse
import argument_preprocessing as argpre
import user_stories
import utilities as utils
import dataframe_helper as dfh

month_to_number = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}


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

    elif args.mode == "fourier":
        # Works with the following command: python python src/raindeer.py
        # 'precipitation' --mode fourier -b 'hessen' 'deutschland'
        if args.month:
            interval = "monthly"
        else:
            interval = "annual"
        columns = args.bundesland
        if args.weather == ["air_temperature_mean"]:
            case = 'temp'
        elif args.weather == ["precipitation"]:
            case = 'rain'
        else:
            case = 'sun'
        user_stories.fourier_analysis(data, interval, columns, case)

    elif args.mode == "between-years":
        # Works with the following command: python src/raindeer.py
        # 'precipitation' --mode between-years -m january  -b 'deutschland'
        # -w 'precipitation' -y 2000..2001
        if args.month:
            interval = "monthly"
        else:
            interval = "annual"
        months = [month_to_number[m] for m in args.month]
        yearsmonths = [str(args.year[0] * 100 + months[0]),
                       str(args.year[-1] * 100 + months[-1])]
        state = args.bundesland[0]
        if args.weather == ["air_temperature_mean"]:
            case = 'temp'
        elif args.weather == ["precipitation"]:
            case = 'rain'
        else:
            case = 'sun'
        mode = args.complexity[0]
        user_stories.plot_between_years(data, interval, yearsmonths, state,
                                        case, mode)
    elif args.mode == "dataframe_helper":
        # Works with raindeer.py --mode dataframe_helper -dt precipitation
        # -i annual -m january february
        # should also work with -dt precipitation hot_days summer_days
        # -i annual monthly
        interval_range = [i for i in args.interval]
        if args.month:
            month_range = [month_to_number[m] for m in args.month]
        else:
            month_range = ['01']
        data_range = [d for d in args.data_type]
        dfh.dataframe_helper(data_range, interval_range, month_range, "wlci")
        print("done")

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
    parser.add_argument('--complexity', '-c', help="""mode for the plot;
                        can be 'simple' or 'custom'""",
                        type=str, nargs="+", default=['simple'])
    parser.add_argument('--interval', '-i', help='interval: monthly and'
                                                 ' or annual',
                        type=str, nargs="+", default=None)
    parser.add_argument('--data_type', '-dt', help='Data Type: precipiation',
                        type=str, nargs="+", default=None)

    args = parser.parse_args()
    if args.url:
        print("input url: ", args.url)
        main(args.url)

    elif args.infile:
        print("inputfile: ", args.infile)
        main(args.infile)

    elif args.mode:
        main(args.mode)
    else:
        print("No url or file provided")
        parser.print_help()
