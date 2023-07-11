#!/usr/bin/python3
""" Module containing a function called write_file"""


def write_file(filename="", text =""):
    """ Function that write into  a file """

    with open(filename, 'w') as wf:
        write_f = wf.write(text)
        return write_f
