import requests
from pathlib import Path
import argparse
#for testing purposes 
from global_var import YEARLY, MONTHLY, MONTHS, ROOT_DATA


# download files from url_list YEARLY
def downloader(url_list, months, dir):
    ## IF url_list is a list do for loop if single item not
    url_list, months = input_checker(url_list, months)

    print(url_list, months, dir)
    for url in url_list:
        ## Get directory from url
        time_dir = url.split('/')[-3]
        ## Get sub directory from url
        sub_dir = url.split('/')[-2]
   
        match time_dir:
            case "annual":
                filename = url.split('/')[-1]
                path = f"{dir}/{time_dir}/{sub_dir}/{filename}"
                url_checker_handler(path, url)

            case "monthly":
                for n in months:
                    monthly_url = url.format(n)
                    filename = monthly_url.split('/')[-1]
                    path = f"{dir}/{time_dir}/{sub_dir}/{filename}"
                    url_checker_handler(path, monthly_url)


def input_checker(url_list, months):
    if isinstance(url_list, str) and isinstance(months, list):
        url_list = string_list_converter(url_list)
         
    elif isinstance(url_list, list) and isinstance(months, str):
        months = string_list_converter(months)
    
    elif isinstance(url_list, str) and isinstance(months, str):
        url_list = string_list_converter(url_list)
        months = string_list_converter(months)

    else:
        pass

    return url_list, months


def string_list_converter(input):
    conv_list = []
    conv_list += [input]
    return conv_list


def url_checker_handler(path, url):
    response = requests.get(url)
    if response.status_code == 200 and url.endswith('.txt'):
        content = response.text
        data_writer(path, content)
    
    else:
        errorfile = url.split('/')[-1]
        print(f"Error downloading file: {errorfile}.")
        

def data_writer(path, url):
    output_file = Path(path)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(url)
    print(f"Downloaded '{path}' STATUS OK.")


#downloader("test", '01', "test")
#downloader(['https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_{}.txt'], '01', "test")

## ADD __IF__ to call it from terminal and from other programs
#if __name__ == "__main__":
    

