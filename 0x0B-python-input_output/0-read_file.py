#!/usr/bin/python3
"""read_file function module"""


def read_file(filename=""):
    """ reads and prints text file """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
