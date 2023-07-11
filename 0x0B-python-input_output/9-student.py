#!/usr/bin/python3
""" Module containing a class called Student"""


class Student:
    """ Student class is created"""

    def __init__(self, first_name, last_name, age):
        """ constructor """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retreving a dictionary representation
        of a Student instance"""

        return self.__dict__
