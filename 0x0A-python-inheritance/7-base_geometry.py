#!/usr/bin/python3
""" Module containing a class called BaseGeometry """


class BaseGeometry:
    """ the class is created"""
    def __init__(self):
        """ constructor """
        pass

    def area(self):
        """ method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that check if the value is integer or not"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
