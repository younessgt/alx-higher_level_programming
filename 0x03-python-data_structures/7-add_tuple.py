#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        new = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    if len(tuple_a) == 1 and len(tuple_b) >= 2:
        new = tuple_a[0] + tuple_b[0], tuple_b[1]
    if len(tuple_a) >= 2 and len(tuple_b) == 1:
        new = tuple_a[0] + tuple_b[0], tuple_a[1]
    if len(tuple_a) == 1 or len(tuple_b) == 1:
         new = tuple_a[0] + tuple_b[0], 0
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        if len(tuple_a) == 0:
            new = tuple_b
        else:
            new = tuple_a
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        new = (0, 0)
    return new
