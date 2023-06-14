#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = []
    summ = 0
    for i in range(len(my_list)):
        if my_list[i] not in n_list:
            n_list.append(my_list[i])
    for i in n_list:
        summ += i
    return summ
