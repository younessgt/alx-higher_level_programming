#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list)
    my_list = my_list[:: -1]
    for i in range(j):
        print("{:d}".format(my_list[i]))
