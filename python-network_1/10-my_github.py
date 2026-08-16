#!/usr/bin/python3
"""
Module using GitHub API with Basic Auth to fetch user ID.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))
