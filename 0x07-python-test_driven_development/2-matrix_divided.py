#!/usr/bin/python3
def check_types(err, type_list, *argv):
    for i in argv:
        if i is None:
            raise TypeError(err)
        t = type(i)
        if t not in type_list:
            raise TypeError(err)
    return (True)


def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if type(matrix[0]) is not list or type(matrix[1]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    check_types("div must be a number", [int, float], div)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    box = []
    length = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for col in matrix[i]:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            check_types(err, [int, float], col)
            row.append(round(col / div, 2))
        box.append(row)
    return box
