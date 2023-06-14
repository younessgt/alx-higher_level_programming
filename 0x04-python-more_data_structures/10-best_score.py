#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    list_val = list(a_dictionary.values())
    list_key = list(a_dictionary.keys())

    for i in range(len(a_dictionary)):
        key = list_key[i]
        value = list_val[i]
        if value == max(list_val):
            return key
