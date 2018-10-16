#!/usr/bin/python3
"""Module with MyList class"""


class MyList(list):
    """ like lists only better """

    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))
