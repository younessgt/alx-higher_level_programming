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

    @property
    def size(self):
        """ retriving the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the value"""
        if isinstance(value, int):
            self.__size = value
        else:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """ Returning the square area"""
        return self.__size ** 2

    def my_print(self):
        """ Printing the square with the carracter #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size - 1):
                    print("#", end="")
                print("#")
