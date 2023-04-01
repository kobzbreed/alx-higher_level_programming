#!/usr/bin/python3
"""
4-hbtn_status module
"""
import requests


if __name__ == "__main__":
    """ Fetches https://alx-intranet.hbtn.io/status """

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
