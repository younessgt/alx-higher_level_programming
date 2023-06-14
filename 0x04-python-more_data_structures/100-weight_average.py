#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    summ = 0
    div = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i]) - 1):
            summ += my_list[i][j] * my_list[i][j + 1]
            div += my_list[i][j + 1]
    tot = summ / div
    return tot
