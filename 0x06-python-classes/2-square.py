#!/usr/bin/python3
""" creating a class named Square that defines a square"""


class Square:
    """ Square class is now created"""
    def __init__(self, size=0):
        """ Initializing the data.
        Args:
                size (int): size of square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
