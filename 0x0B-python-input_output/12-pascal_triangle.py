#!/usr/bin/python3
""" Module containing function called pascal_triangle"""


def pascal_triangle(n):
    """ pascal triangle function """

    if n <= 0:
        return []
    my_list = [[1]]
    for r in range(n-1):
        list_1 = [1]
        for i in range(r):
            list_1.append(my_list[-1][i] + my_list[-1][i+1])
        list_1.append(1)
        my_list.append(list_1)
    return my_list
