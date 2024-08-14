#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(dict_sc, total_file_size):
    """
    Prints the accumulated metrics
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print('File size: {}'.format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print('{}: {}'.format(key, val))


total_file_size = 0
code = 0
count = 0
dict_sc = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
           '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Trimming
        parsed_line = parsed_line[::-1]  # Tnverting

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_file_size += int(parsed_line[0])  # File size
                code = parsed_line[1]  # Status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (count == 10):
                print_stats(dict_sc, total_file_size)
                count = 0

finally:
    print_stats(dict_sc, total_file_size)
