#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lists = []
    length = len(a_dictionary)
    list_key = list(a_dictionary.keys())
    list_val = list(a_dictionary.values())
    for i in range(length):
        lists.append("{}: {}".format(list_key[i], list_val[i]))
    sor = sorted(lists)
    for i in range(len(lists)):
        print(sor[i])
