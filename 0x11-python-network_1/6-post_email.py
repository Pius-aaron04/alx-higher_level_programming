#!/usr/bin/python3
"""
posts data to the provided URL
"""

import sys
import requests

if __name__ == '__main__':
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
