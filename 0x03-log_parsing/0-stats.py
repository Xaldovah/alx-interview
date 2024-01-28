#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

from sys import stdin

file_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
                "405": 0, "500": 0}
status_code = 0
line_count = 0


def stats(file_size, status_codes):
    """
    Prints the statistics from the beginning and after every 10 lines
    and/or a keyboard interrupt
    """
    print("File size: " + str(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(code + ": " + str(status_codes[code]))


try:
    for line in stdin:
        line_count += 1
        split_line = line.split()

        if len(split_line) > 1:
            file_size += int(split_line[-1])

        if len(split_line) > 2 and split_line[-2].isdigit():
            status_code = split_line[-2]
        else:
            status_code = 0

        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            stats(file_size, status_codes)

        stats(file_size, status_codes)


except KeyboardInterrupt:
    stats(file_size, status_codes)
    raise
