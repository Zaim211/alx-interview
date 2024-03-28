#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys


# 0 is default value of each key
status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
# total_size: to accumulate the total size of the files processed
total_size = 0
# Counter used to determine when to print metrics (every 10 lines)
counter = 0


try:
    for line in sys.stdin:
        lines = line.split(" ")
        if len(lines) > 4:
            extract_code = lines[-2]
            int_size = int(lines[-1])
            if extract_code in status_code.keys():
                status_code[extract_code] += 1
            total_size += int_size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except Exception:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
