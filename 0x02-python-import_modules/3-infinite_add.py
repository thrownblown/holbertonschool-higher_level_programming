#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_c = len(argv)
    a = 0;
    for i in range(1, arg_c):
        try:
            a += int(argv[i])
        except ValueError:
            a = float(a) + float(argv[i])
    print(a)
