#!/usr/bin/python3
""" Module containing a function called save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """ function that write an object to a file
    using JSON"""

    with open(filename, 'w') as wf:

        json.dump(my_obj, wf)
