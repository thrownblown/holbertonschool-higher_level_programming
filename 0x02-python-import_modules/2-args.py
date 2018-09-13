#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_c = len(argv)
    if arg_c > 2:
        print("{} arguments:".format(arg_c - 1))
        for i in range(1, arg_c):
            print("{}: {}".format(i, argv[i]))
    elif arg_c == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("0 arguments.")
