#!/usr/bin/python3

"""
this module contain a function called matrix_divided
function:
    matrix_divided(matrix, div): this function divides all
    element of a matrix
"""


def matrix_divided(matrix, div):
    """
    function used to divide all element of a matrix
    """

    new_matrix = []
    if type(matrix) == list and (not any(matrix) or not any(matrix[0])):
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for mat in matrix:
        if type(matrix) != list or type(mat) != list:
            raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
        row = []
        for i in mat:

            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")

            if len(mat) != len(matrix[0]):
                raise TypeError("Each row of the matrix\
                        must have the same size")
            row.append(round(i / div, 2))
        new_matrix.append(row)
    return new_matrix
