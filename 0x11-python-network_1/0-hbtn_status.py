#!/usr/bin/python3
"""Accesses URL (https://alx-intranet.hbtn.io/status) and displays info"""

import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(content.decode('utf8')))
