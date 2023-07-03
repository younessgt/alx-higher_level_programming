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
        if self.__width == 0 or self.__height == 0:
            return 0
        p = 2 * (self.__width + self.__height)
        return p

    def __str__(self):
        """
        special method that convert a rectangle object into
        string
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for i in range(self.__height):
                if i < self.__height - 1:
                    string += "#" * self.__width + "\n"
                else:
                    string += "#" * self.__width
            return string

    def __repr__(self):
        """ special method that return a string
        representation of the rectangle
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ special method is called when an object is destroyed"""

        print("Bye rectangle...")
