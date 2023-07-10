#!/usr/bin/python3
""" Module containing is_same_class function """


def is_same_class(obj, a_class):
    """ function that check if the object is an instance
    of the specified class or not

    obj: is the object to check
    a_class: specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
