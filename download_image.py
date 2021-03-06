#!/usr/bin/env python3
"""
This is a script to continually attempt to download files from
a running instance of caom2repo.
"""

from datetime import datetime, timedelta
import argparse
import time
import requests

def get_arguments():
    """ Get arguments from command line """
    parser = argparse.ArgumentParser(description='Download some files from caom2repo')
    parser.add_argument('--period', action='store', dest='period', type=int, default=5,
                        help='minimum period in seconds between request events')
    parser.add_argument('--url', action='store', dest='url', default='http://localhost:8080',
                        help='minimum period in seconds between request events')
    return parser.parse_args()

def repeatedly_download(url, period):
    """ Repeatedly download a file from a url, with minimum period between downloads in seconds"""
    while True:
        loop_beginning_time = datetime.now()
        response = requests.get(url)
        print response.content
        remaining_time = datetime.now() - loop_beginning_time
        if remaining_time <= timedelta(seconds=period):
            time.sleep((timedelta(seconds=period) - remaining_time).total_seconds())

def main():
    "Main function for downloading images from caom2repo"
    args = get_arguments()
    repeatedly_download(args.url, args.period)


if __name__ == "__main__":
    main()
