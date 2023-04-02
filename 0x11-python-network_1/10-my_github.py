#!/usr/bin/python3
"""
10-my_guthub module
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    """
    Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
    """

    authenticate = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=authenticate)
    print(r.json().get("id"))
