#!/usr/bin/python3
""" Module containing a function called read_file"""


def read_file(filename=""):
    """ Function that reads a file """

    with open(filename, 'r') as rf:
        read_f = rf.read()
        print(read_f, end='')
