"""
DOCSTRING ....
"""
from utilities import yaml_reader


def arg_preprocess(args):
    """transforms input arguments
       and handels many errors"""
    arg_test_year(args)
    arg_test_month(args)
    arg_test_weather(args)
    arg_test_bundesland(args)


def arg_test_year(args):
    if args.year:
        year = []
        for i in range(0, len(args.year)):
            if args.year[i].find('..') != -1:
                ran = args.year[i].split("..")
                check_if_year(ran[0])
                check_if_year(ran[1])
                start = int(ran[0])
                end = int(ran[1])
                for j in range(start, end + 1):
                    year.append(j)

            else:
                check_if_year(args.year[i])
                year.append(int(args.year[i]))

        args.year = sorted(set(year))


def check_if_year(_year):
    assert _year.isdigit(), str(_year) + " is not a number"


def arg_test_month(args):
    if args.month:
        month = []
        calendar = yaml_reader('month_names')
        for i in range(0, len(args.month)):
            args.month[i] = args.month[i].lower()
            if args.month[i].find('..') != -1:
                ran = args.month[i].split("..")
                start = check_if_month(ran[0], calendar)
                end = check_if_month(ran[1], calendar)
                for j in range(start, end + 1):
                    month.append(calendar[j])

            else:
                check_if_month(args.month[i], calendar)
                month.append(args.month[i])

        args.month = sorted(set(month), key=lambda inp: calendar.index(inp))


def check_if_month(_month, _cal):
    for i in range(0, len(_cal)):
        if _month == _cal[i]:
            return i
    assert str(_month) + " is not a month"


def arg_test_weather(args):
    if args.weather:
        weather = []
        weather_options = yaml_reader('monthly_data_type')
        for i in range(0, len(args.weather)):
            args.weather[i] = args.weather[i].lower()
            weather.append(weather_options[
                               check_if_weather(args.weather[i],
                                                weather_options)])

        args.weather = sorted(set(weather),
                              key=lambda inp: weather_options.index(inp))


def check_if_weather(_weather, _weather_options):
    for i in range(0, len(_weather_options)):
        if _weather in _weather_options[i]:
            return i
    assert str(_weather) + " is not a weather"


def arg_test_bundesland(args):
    if args.bundesland:
        bundesland = []
        bund = yaml_reader('headers')
        bundesland_options = bund[1:]
        for i in range(0, len(args.bundesland)):
            args.bundesland[i] = args.bundesland[i].lower().replace("ü", "ue")
            if args.bundesland[i] in ["all", "alle", "every"]:
                bundesland = bundesland_options[:-1]
                break
            check_if_bundesland(args.bundesland[i], bundesland_options)
            bundesland.append(args.bundesland[i])

        args.bundesland = sorted(set(bundesland),
                                 key=lambda inp: bundesland_options.index(inp))


def check_if_bundesland(_bundesland, _bundesland_options):
    for i in range(0, len(_bundesland_options)):
        if _bundesland == _bundesland_options[i]:
            return i
    assert str(_bundesland) + " is not a bundesland"
