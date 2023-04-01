#!/usr/bin/python3
"""
7-error_code module
"""
import requests
import sys


if __name__ == "__main__":
    """
    Sends a request to the URL passed as an argument and
    displays the body of the response.
    """
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
