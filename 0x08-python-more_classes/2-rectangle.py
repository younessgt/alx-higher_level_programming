#!/usr/bin/python3
""" This module contain a class that defines a rectangle"""


class Rectangle:
    """ class called Rectangle has been created"""

    def __init__(self, width=0, height=0):
        """ initializing the data """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ retreiving the width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ setting a value to the width """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retreiving the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting a value to the width """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """ method that returns the rectangle perimeter"""

        p = 2 * (self.__width + self.__height)
        return p
