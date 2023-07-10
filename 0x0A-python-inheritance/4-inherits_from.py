#!/usr/bin/python3
""" Module containig inherits_from function """


def inherits_from(obj, a_class):
    """ function that return True if:
    the object is an instance of a class that is a subclass of
    the specified class

    else it return False
    """

    x = obj.__class__
    if x == a_class:
        return False
    if issubclass(x, a_class):
        return True
    else:
        return False
