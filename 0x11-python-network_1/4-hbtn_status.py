#!/usr/bin/python3
"""
Fetches content from URL using requests package
"""

import requests

request = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:\n\t- type: {}\n\t- content: {}".format(type(request.
                                                                  text),
                                                             request.text))
