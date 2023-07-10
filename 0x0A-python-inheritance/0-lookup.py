#!/usr/bin/python3
""" Module containing lookup Function"""


def lookup(obj):
    """function that returns 
    the list of available attributes and methods of an object
    """
    return dir(obj)
