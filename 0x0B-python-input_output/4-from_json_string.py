#!/usr/bin/python3
""" Module containing a function called from_json_string"""

import json


def from_json_string(my_obj):
    """ function that return an object represented
    by JSON string"""

    json_loads = json.loads(my_obj)
    return json_loads
