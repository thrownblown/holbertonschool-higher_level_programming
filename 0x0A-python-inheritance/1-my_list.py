#!/usr/bin/python3
class MyList(list):
    """ like lists only better """

    def print_sorted(self):
        retval = self[:]
        retval.sort()
        print(retval)
