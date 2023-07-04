#!/usr/bin/python3
""" module containing a class that prevent user from
creating new instance"""


class LockedClass:
    """ prenventing user from creation new instance except if
    the new instance is called 'first_name'
    """
    __slots__ = ('first_name')

    def __init__(self):
        pass
