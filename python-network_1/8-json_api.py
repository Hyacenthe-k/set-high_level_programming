#!/usr/bin/python3
"""
Module to send a POST request with a letter search parameter using requests.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    
    try:
        r = requests.post(url, data={'q': q})
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
