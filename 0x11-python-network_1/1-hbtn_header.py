#!/usr/bin/python3
"""
1-hbtn_header module
"""
import urllib.request
import sys


if __name__ == "__main__":
    """
    sends a request to the URL passed as an argument and displays
    the value of the 'X-Request-Id' variable found in the header
    of the response
    """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
