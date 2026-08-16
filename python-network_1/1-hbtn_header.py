#!/usr/bin/python3
"""
Module to fetch X-Request-Id header from a URL using urllib.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
