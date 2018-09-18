#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for col in range(0, len(row) - 1):
                print("{:d} ".format(row[col]), end="")
            print("{:d}".format(row[-1]))
        else:
            print("")
            break
