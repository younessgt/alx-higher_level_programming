#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda n_matr: list(map(lambda p: p ** 2, n_matr)), matrix))
