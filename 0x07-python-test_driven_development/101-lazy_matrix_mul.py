#!/usr/bin/python3
""" This module conatin a function called lazy_matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ function that multiplies e matrices
    using the module Numpy
    argument:
        m_a: first 2d array
        m_b: second 2d array
    """

    arr = np.matmul(m_a, m_b)
    return arr
