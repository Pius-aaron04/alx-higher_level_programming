#!/usr/bin/python3
"""
Takes in a URL and an email. Then sends email vai a post request to the server.
"""

import sys
import urllib.request

values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)

with urllib.request.urlopen(req) as response:
    print(response.read())
