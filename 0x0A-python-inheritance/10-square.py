#!/usr/bin/python3
""" Module containing a class named
Square that inherited from Rectangle class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class is created """

    def __init__(self, size):
        """ constructor """
        x = super().integer_validator("size", size)
        # we can use always Ractangle.integer_validator(...)
        # or self.integer_validator(...)
        if x is None:
            self.__size = size
            super().__init__(size, size)

    def area(self):
        """ method to calculate the square area """
        return self.__size * self.__size
