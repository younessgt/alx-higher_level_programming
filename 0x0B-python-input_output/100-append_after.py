#!/usr/bin/python3
""" Module containing a function called append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ function that insert a line text to file after each
    line containing a specific string"""

    with open(filename, "r") as rf:
        read_file = rf.readlines()
    with open(filename, "w") as wf:
        for line in read_file:
            wf.write(line)
            if search_string in line:
                wf.write(new_string)
