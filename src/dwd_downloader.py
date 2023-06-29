import requests
from pathlib import Path
from bs4 import BeautifulSoup
import urllib.parse

# download files from url_list YEARLY
def dwd_downloader(url_list, months, dir):
    ## convert url_list or month into lists if necessary
    url_list, months = input_checker(url_list, months)
    # iterate over the url_list
    for url in url_list:
        ## Get directory from url
        time_dir = url.split('/')[-3]
        ## Get sub directory from url
        sub_dir = url.split('/')[-2]
        #switch implementation for monthly or yearly 
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

