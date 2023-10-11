#!/usr/bin/python3
"""
This is a script that reads log and outputs metrics.
"""

import sys


status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
total_file_size = 0
lines = 0
for line in sys.stdin:
    lines += 1
    log = line.split()
    total_file_size += int(log[-1])
    status_codes[int(log[-2])] += 1

    if lines % 10 == 0:
        print("File size: {}".format(total_file_size))
        for key, value in status_codes.items():
            print("{}: {}".format(key, value))
