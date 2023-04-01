#!/usr/bin/python3
"""
6-post_email module
"""
import requests
import sys


if __name__ == "__main__":
    """
    Sends a POST request to the passed URL with the email as
    a parameter, and finally displays the body of the response.
    """
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, value)
    print(r.text)
