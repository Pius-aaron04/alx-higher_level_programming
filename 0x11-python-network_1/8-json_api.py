#!/usr/bin/python3
"""
sends a post request to a sever.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No result")
    else:
        data = sys.argv[1].split('=')
        if len(data) == 2:
            data = {data[0]: data[1]}
        else:
            data = {data[0]: ""}
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data=data)
        try:
            json = r.json()
            if json:
                print(json)
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
