#!/usr/bin/env python3

import sys

total_size = 0
status_code_counts = {}
line_count = 0
last_printed_codes = set()

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7 and parts[2] == '-[':
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size
                status_code_counts[status_code] = status_code_counts.get(
                        status_code, 0) + 1

                if status_code not in last_printed_codes or line_count % 10 == 0 or line_count == 1:
                    print("File size:", total_size)
                    for code in sorted(status_code_codes):
                        print(f"{code}: {status_code_counts[code]}")
                        print()
                        line_count = 0
            except ValueError:
                pass

except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
