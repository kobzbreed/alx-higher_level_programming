#!/usr/bin/python3
"""
8-json_api module
"""
import requests
import sys


if __name__ == "__main__":
    """
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    letter = "" if len(sys.argv) == 1 else (sys.argv[1])
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
