#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = {}
    list_val = list(a_dictionary.values())
    list_key = list(a_dictionary.keys())
    for i in range(len(a_dictionary)):
        list_val[i] *= 2
        key = list_key[i]
        value = list_val[i]
        copy_dict.update({key: value})
    return copy_dict
