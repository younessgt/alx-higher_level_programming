#!/usr/bin/python3
""" Module containinf function called class_to_json"""


def class_to_json(obj):
    """ function that return a dictionary discription
    for JSON object"""

    return obj.__dict__
