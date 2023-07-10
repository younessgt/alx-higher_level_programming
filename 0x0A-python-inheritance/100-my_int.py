#!/usr/bin/python3
""" Module containing a class clled MyInt that inherits from int"""


class MyInt(int):
    """ MyInt is created """
    def __eq__(self, other):
        """ opposite of __eq__ magic method """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ opposite of __ne__ magic method """
        return not super().__ne__(other)
