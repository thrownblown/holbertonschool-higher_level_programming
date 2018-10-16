#!/usr/bin/python3
"""number_of_lines function module"""


def number_of_lines(filename=""):
    """ returns number of lines in text file """
    with open(filename, encoding='utf-8') as f:
        return(len(f.readlines()))
