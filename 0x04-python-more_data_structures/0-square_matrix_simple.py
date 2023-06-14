#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    length = len(matrix)
    length1 = len(matrix[0])
    new_matrix = []

    for i in range(length):
        row = []
        for j in range(length1):
            row.append(matrix[i][j] ** 2)
        new_matrix.append(row)
    return new_matrix
