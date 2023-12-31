"""
Processes and visualizes different data
relating to the climate

Offering the CLI entry point!
"""

import logging
import argparse
import raindeer.argument_preprocessing as argpre
import raindeer.user_stories as user_stories
import raindeer.utilities as utils
import raindeer.dataframe_helper as dfh

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


def parse_command_line():
    """
    Parse the command line for input arguments.

    Returns:
        args
    """
    logging.basicConfig(filename='raindeer.log', level=logging.INFO)
    logging.info('Reading command-line arguments.')

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
    parser.add_argument('--data_set', '-ds', help='Data Type: precipitation',
                        type=str, nargs="+", default=None)

    args = parser.parse_args()

    return args


def main():
    """
    Executes different operations based on the mode specified through
    command line arguments.

    Raises:
        ValueError: If the mode specified is not valid.

    Example:
        >>> main("data/annual/air_temperature_mean/
            regional_averages_tm_year.txt")
    """
    args = parse_command_line()

    if args.url:
        print("input url: ", args.url)
        data = args.url

    elif args.infile:
        print("inputfile: ", args.infile)
        data = args.infile

    elif args.mode:
        data = args.mode

    else:
        logging.error('No URL or file provided.')
        print('No URL or file provided.')

    argpre.arg_preprocess(args)

    if args.mode == "forecast":
        """"
        Performs forecasting based on the specified data.

        Example:
            >>> args.year = 2022
            >>> args.bundesland = ['Deutschland']
            >>> main("data/annual/air_temperature_mean/
                regional_averages_tm_year.txt")
        """
        logging.info('Selected mode: forecast')
        # Works with the following command: python raindeer/raindeer.py
        # "data/annual/air_temperature_mean/regional_averages_tm_year.txt"
        # --mode=forecast -b='Deutschland'
        time = args.year
        place = args.bundesland[0].title()
        means = utils.load_dataset(data).loc[time, place].to_numpy()
        print(user_stories.linear_regression(time, means, args.forecast,
                                             'Time in years',
                                             'Temperature mean in °C'))

    elif args.mode == "plot-params":
        """
        Plots weather parameters for the specified time and place.

        Example:
            >>> args.year = 2022
            >>> args.bundesland = ['Baden-Wuerttemberg']
            >>> main("data/annual")
        """
        logging.info('Selected mode: plot-params')
        # Works with the following command: python raindeer/raindeer.py
        # "data/annual" --mode=plot-params -b='Baden-Wuerttemberg'
        time = args.year
        place = args.bundesland[0].title()
        user_stories.plot_weather_parameters_annual(time, place, data)

    elif args.mode == "fourier":
        """
        Performs Fourier analysis on the specified data.

        Example:
            >>> args.month = True
            >>> args.bundesland = ['hessen', 'deutschland']
            >>> args.weather = ['precipitation']
            >>> main("data/annual")
        """
        logging.info('Selected mode: fourier')
        # Works with the following command: python python raindeer/raindeer.py
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
        """
        Plots weather data between the specified years.

        Example:
            >>> args.month = True
            >>> args.year = [2000, 2001]
            >>> args.bundesland = ['deutschland']
            >>> args.weather = ['precipitation']
            >>> args.complexity = ['january']
            >>> main("data/annual")
        """
        logging.info('Selected mode: between-years')
        # Works with the following command: python raindeer/raindeer.py
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
        """
        Performs operations on the dataframe based on the specified parameters.

        Example:
            >>> args.interval = ['annual']
            >>> args.month = ['january', 'february']
            >>> args.data_set = ['precipitation']
            >>> main("data/annual")
        """
        logging.info('Selected mode: dataframe_helper')
        # Works with raindeer.py --mode dataframe_helper -dt precipitation
        # -i annual -m january february
        # should also work with -dt precipitation hot_days summer_days
        # -i annual monthly
        interval_range = [i for i in args.interval]
        if args.month:
            month_range = [month_to_number[m] for m in args.month]
        else:
            month_range = ['01']
        data_range = [d for d in args.data_set]
        dfh.dataframe_helper(data_range, interval_range, month_range, "wlci")
        print("done")

    elif args.mode == "simple-plot":
        # Works with the following command: python src/raindeer.py
        # "data/annual" --mode=simple-plot -y 2000 -m "January"
        # -b "Brandenburg" -w "precipitation"
        user_stories.simple_plot(data, args, month_to_number)

    elif args.mode == "download-all":
        dfh.dataframe_helper(utils.yaml_reader('all_data_types'),
                             utils.yaml_reader('interval'),
                             utils.yaml_reader('months'),
                             "dl")

    else:
        logging.error(str(args.mode) + ' is not a valid mode!')
        print(str(args.mode) + ' is not a valid mode!')


# CLI entry point
# more options should be added here later.
if __name__ == "__main__":
    main()
