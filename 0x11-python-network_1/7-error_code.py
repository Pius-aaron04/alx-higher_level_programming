#!/usr/bin/python3
"""
Displays the content of a URL or Error code
"""
import sys
import requests

if __name__ == '__main__':
    req = requests.get(sys.argv[1])

    if not req.status_code >= 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
