#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret_matrix = []
    for idx, row in enumerate(matrix):
        ret_matrix.append([])
        for col in row:
            ret_matrix[idx].append(col ** 2)
    return(ret_matrix)
