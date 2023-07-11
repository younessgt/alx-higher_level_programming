#!/usr/bin/python3
""" Module containing a function called load_from_json_file"""

import json


def load_from_json_file(filename):
    """ function that create an object fro JSON file"""

    with open(filename, 'r') as rf:

        return json.load(rf)
