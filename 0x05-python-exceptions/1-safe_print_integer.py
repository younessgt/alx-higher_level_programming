#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value
        print("{:d}".format(int(value)))
        return True
    except Exception as er:
        return False
