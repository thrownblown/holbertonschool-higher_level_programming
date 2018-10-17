#!/usr/bin/python3
""" read_lines function module """
read_file = __import__('0-read_file').read_file
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file and prints """
    if not nb_lines or number_of_lines(filename) < nb_lines:
        read_file(filename)
    with open(filename, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < nb_lines or nb_lines <= 0:
                print(line, end='', sep='')
            else:
                break
