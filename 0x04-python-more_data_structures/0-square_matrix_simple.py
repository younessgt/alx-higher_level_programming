#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    length = len(matrix)
    length1 = len(matrix[0])
    new_matrix = [[0] * length for i in range(length)]

    for i in range(length):
        for j in range(length1):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
