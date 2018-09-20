#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == '__main__':
    calculator = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in calculator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        retval = calculator[argv[2]](int(argv[1]), int(argv[3]))
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], retval))
