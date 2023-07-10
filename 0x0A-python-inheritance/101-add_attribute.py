#!/usr/bin/python3
""" Module Containing a function called add_attribute"""


def add_attribute(cls, attr, val):
    """ function that add an attribute to the specified object
    if it's possible """

    if hasattr(cls, '__dict__'):
        # if an object has the __dict__ attribute it means it is extensible.
        # so we can add attributes to
        # that object and it will be stored on __dict__

        cls.__dict__[attr] = val

        # or we can use getattr(cls, attr, val) instead of
        # cls.__dict__[attr] = val

        return f"{cls.__dict__[attr]}"
    else:
        raise TypeError("can't add new attribute")
