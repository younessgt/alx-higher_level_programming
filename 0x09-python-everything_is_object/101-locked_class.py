#!/usr/bin/python3
""" module containing a class called LockedClass"""


class LockedClass:
    """ prenventing user from creation new instance
    attributes except for 'first_name'
    """
    __slots__ = ('first_name')

    def __init__(self):
        pass
