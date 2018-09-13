#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_c = len(argv)
    if arg_c > 1:
        print("{} arguments:".format(arg_c))
        for i in range(arg_c):
            print("{}: {}".format(i, argv[i]))
    elif arg_c == 1:
        print("{} argument:".format(arg_c))
        print("1: {}".format(argv[0]))
    else:
        print("0 arguments.")
