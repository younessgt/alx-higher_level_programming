#!/usr/bin/python3
""" Module containing is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ function that return True if :
    -> the object is an instance of the specified class
    -> the object is an instance of a class that inherited from
    the specified class

    else it return False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
