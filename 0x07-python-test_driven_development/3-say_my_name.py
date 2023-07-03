#!/usr/bin/python3
"""
this module contain a function called say_my_name that
print the fullname
function:
    say_my_name: function that print "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    This function print a fullname
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
