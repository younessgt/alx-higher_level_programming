#!/usr/bin/python3
""" Module containing a function called to_json_string"""

import json


def to_json_string(my_obj):
    """ function that return a JSON representation
    of an object(string)"""

    json_dumps = json.dumps(my_obj)
    return json_dumps
