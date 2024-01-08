#!/usr/bin/python3
"""
sends a post request to a sever.
"""

import requests
import sys

r = requests.post('http://0.0.0.0:5000/search_user', data={sys.argv[1]: ""})
print(r.text)
