#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        j += 1
    for k in range(x):
        try:
            print(my_list[k], end='')
        except Exception as er:
            break
    print()
    if x <= j:
        return x
    else:
        return j
