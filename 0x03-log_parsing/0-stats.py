#!/usr/bin/python3
"""This module reads stdin line by line and computes metrics"""

import sys

total_size = 0
status_code_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            print("File size:", file_size)
            print(f"{status_code}")
        except ValueError:
            pass

        if len(parts) >= 7 and parts[2] == '-[':
            print(parts)
            try:
                total_size += file_size
                status_code_counts[status_code] = status_code_counts.get(
                        status_code, 0) + 1
            except ValueError:
                pass

            if line_count % 10 == 0 or line_count == 1:
                print("File size:", total_size)
                for code in sorted(status_code_counts):
                    print(f"{code}: {status_code_counts[code]}")
                    print()
                    line_count = 0

except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
