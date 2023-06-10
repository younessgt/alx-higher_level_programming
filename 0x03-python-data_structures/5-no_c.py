#!/usr/bin/python3
def no_c(my_string):
    copy_s = ""
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            copy_s += my_string[i]
        else:
            copy_s += ''
    return copy_s
