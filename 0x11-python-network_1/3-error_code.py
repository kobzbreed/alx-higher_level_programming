#!/usr/bin/python3
"""
3-error_code module
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    """
    Sends a request to the URL passed as an argument and
    displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
