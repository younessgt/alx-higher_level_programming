#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list:
        if isinstance(i, int):
            j += 1
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end='')
        except IndexError:
            raise
        except Exception as e:
            pass
    print()
    if x <= j:
        return x
    else:
        return j
