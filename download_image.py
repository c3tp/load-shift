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
    parser.add_argument('--url', action='store', dest='url', default='localhost:8080',
                        help='minimum period in seconds between request events')
    return parser.parse_args()

def repeatedly_download(url, period):
    """ Repeatedly download a file from a url, with minimum period between downloads in seconds"""
    while True:
        loop_beginning_time = datetime.now()
        response = requests.get(url)
        print response
        target_loop_continue_time = loop_beginning_time + timedelta(seconds=period)
        if target_loop_continue_time > 0:
            time.sleep(target_loop_continue_time)

def main():
    "Main function for downloading images from caom2repo"
    args = get_arguments()
    repeatedly_download(args.url, args.period)


if __name__ == "__main__":
    main()
