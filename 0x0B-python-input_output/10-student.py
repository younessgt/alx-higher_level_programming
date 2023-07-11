#!/usr/bin/python3
""" Module containing a class called Student"""


class Student:
    """ Student class is created"""

    def __init__(self, first_name, last_name, age):
        """ constructor """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """ retreving a dictionary representation
        of a Student instance"""

        if attr is None:
            return self.__dict__
        else:
            new_dict = {}
            for attri in attr:
                if attri in self.__dict__:
                    new_dict.update({attri: self.__dict__[attri]})
            return new_dict
