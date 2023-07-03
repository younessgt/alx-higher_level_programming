#!/usr/bin/python3
"""
This module contain a function that print a square with "#"
function:
    print_square: print a square with "#"
"""


def print_square(size):
    """
    this function print a square with "#"

    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
