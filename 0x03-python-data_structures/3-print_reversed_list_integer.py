#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != []:
        j = len(my_list)
        for i in range(j):
            print("{:d}".format(my_list[j - i - 1]))
