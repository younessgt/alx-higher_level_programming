#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_val = list(a_dictionary.values())
    list_key = list(a_dictionary.keys())
    for i in range(len(a_dictionary)):
        if list_val[i] == value:
            a_dictionary.pop(list_key[i])
    return a_dictionary
