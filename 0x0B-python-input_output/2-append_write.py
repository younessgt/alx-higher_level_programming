#!/usr/bin/python3
""" Module containing a function called append_write"""


def append_write(filename="", text=""):
    """ Function that append a string to a file"""

    with open(filename, 'a') as af:
        append_f = af.write(text)
        return append_f
