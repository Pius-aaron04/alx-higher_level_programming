#!/usr/bin/python3
"""
Sends a request to the url passed at CLI and displays the value of the
X-Request-Id variable found in the header
"""

import sys
import urllib.request
if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(req) as response:
        xRequestID = response.headers.get('X-Request-Id')
        print(xRequestID)
