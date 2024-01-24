#!/usr/bin/python3

import sys
from datetime import datetime


total_size = 0
status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split(' ')

        if len(parts) == 10 and parts[3].isdigit() and parts[8].isdigit():
            ip, date_str, status_code, file_size = parts[
                    0], parts[3], parts[8], int(parts[9])

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # print statistics every 10 lines
            if line_count % 10 == 0:
                print(f'Total file size: {total_size}')
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print(f'{code}: {status_codes[code]}')
                print()

except KeyboardInterrupt:
    print(f'Total file size: {total_size}')
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f'{code}: {status_codes[code]}')
