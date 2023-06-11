#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_l = my_list[0]
    for i in range(1, len(my_list)):
        if max_l > my_list[i]:
            max_l = max_l
        else:
            max_l = my_list[i]
    return max_l
