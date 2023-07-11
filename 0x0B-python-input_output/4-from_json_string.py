#!/usr/bin/python3
""" Module containing a function called from_json_string"""

import json


def from_json_string(my_obj):
    """ function that return a JSON representation
    of an object(string)"""

    json_loads = json.loads(my_obj)
    return json_loads
