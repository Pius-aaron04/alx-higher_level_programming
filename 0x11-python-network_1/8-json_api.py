#!/usr/bin/python3
"""
sends a post request to a sever.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv):
        print("No result")
    try:
        json = r.json()
        if json:
            print(json)
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
