import argparse
from data_helper import *

def main(data, num):
    pass

# CLI entry point  
# more optons should be added here later.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a file or an url')
    parser.add_argument('--url', help='url to process')
    parser.add_argument('--file', help='file to process')
    args = parser.parse_args()
    if args.url:
        print("url: ", args.url)
        main(args.url, 3)
        
    elif args.file:
        print("file: ", args.file)
        main(args.file, 7)

    else:
        print("No url or file provided")
        parser.print_help()

