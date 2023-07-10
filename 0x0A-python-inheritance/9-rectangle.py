#!/usr/bin/python3
""" Module containig a class called  Rectangle
that inherited from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class is created """

    def __init__(self, width, height):
        """ constructor """

        res1 = BaseGeometry.integer_validator(self, "width", width)
        res2 = BaseGeometry.integer_validator(self, "height", height)
        # or we can use super().integer_validator("height", height)
        if res1 is None and res2 is None:
            self.__width = width
            self.__height = height

    def area(self):
        """ method that calculate the area of a rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ giving the object a human readable string """

        return f"[Rectangle] {self.__width}/{self.__height}"
