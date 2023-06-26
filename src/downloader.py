import requests
from pathlib import Path
import argparse
#for testing purposes 
from global_var import YEARLY, MONTHLY, MONTHS, ROOT_DATA


# download files from url_list YEARLY
def downloader(url_list, months, dir):
    for url in url_list:
        ## Get directory from url
        interval_directory = url.split('/')[-1]
        ## Get sub directory from url
        sub_directory = url.split('/')[-2]
        ## Get filename from url
        
  
        match interval_directory:
            case "annual":
                filename = url.split('/')[-1]
                path = f"{dir}/{interval_directory}/{sub_directory}/{filename}"
                valid_y_url = url_checker(url)
                data_writer(valid_y_url, path)
                 

            case "monthly":
                for n in months:
                    monthly_url = url.format(n)
                    filename = monthly_url.split('/')[-1]
                    path = f"{dir}/{interval_directory}/{sub_directory}/{filename}"
                    valid_m_url = url_checker(monthly_url)
                    data_writer(valid_m_url, path)

                          
def url_checker(url):
    response = requests.get(url)
    if response.status_code == 200 and url.endswith('.txt'):
        #print("OK")
        content = response.text
        return content
    
    else:
        errorfile = url.split('/')[-1]
        print(f"Error downloading file: {errorfile}.")
        

def data_writer(url, path):
    output_file = Path(path)
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(url)
    print(f"Downloaded '{path}' STATUS OK.")


## ADD __IF__ to call it from terminal and from other programs
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process three inputs')
    parser.add_argument('input1', help='1 or more URLs')
    parser.add_argument('input2', help='Months wanted in a list  years')
    parser.add_argument('input3', help='Where to downloard to')
    args = parser.parse_args()

    try:
        downloader(args.url, args.input2, args.input3)
    except IndexError:
        print("Invalid URL provided. Make sure the URL has enough components.")
