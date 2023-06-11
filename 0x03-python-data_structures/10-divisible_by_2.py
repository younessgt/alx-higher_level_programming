#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for num in my_list:
        if num % 2 == 0:
            new += [True]
        else:
            new += [False]
    return new
