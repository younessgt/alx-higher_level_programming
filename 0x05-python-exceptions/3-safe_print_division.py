#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except Exception as er:
        pass
    finally:
        if b != 0:
            print("Inside result: {}".format(c))
            return c
        else:
            print("Inside result: {}".format(None))
            return None
