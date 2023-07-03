#!/usr/bin/python3

"""
This module contain a function that add two integer
Function:
    add(a, b): function to add two integers
"""


def add_integer(a, b=98):
    """
    function that add two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
