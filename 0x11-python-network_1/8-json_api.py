#!/usr/bin/python3
"""
sends a post request to a sever.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': ''})
    else:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': sys.argv[1]})
    try:
        json = r.json()
        if json:
            print('[{}] {}'.fomart(json['id'], json['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
