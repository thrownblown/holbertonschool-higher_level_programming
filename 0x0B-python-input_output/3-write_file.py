#!/usr/bin/python3
""" write_file function module """


def write_file(filename="", text=""):
    """ writes text to filename """
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
