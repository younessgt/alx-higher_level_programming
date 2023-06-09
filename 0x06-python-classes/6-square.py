#!/usr/bin/python3
""" creating a class called Square that defines a square"""


class Square:
    """ Square class is now created"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the data.
        Args:
                size (int): size of square
                position : position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retriving the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting the new position"""
        if isinstance(value, tuple) and len(value) == 2\
                and all(isinstance(i, int) and i >= 0 for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returning the square area"""
        return self.__size ** 2

    def my_print(self):
        """ Printing the square with the carracter #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
