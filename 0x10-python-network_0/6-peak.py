#!/usr/bin/python3
"""  python script Containing  find_peak function"""


def find_peak(list_of_integers):
    """ function that find a peak in a list of unsorted
    integers """

    if len(list_of_integers) == 0:
        return None

    for i in range(len(list_of_integers) - 1):
        j = i
        if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]:
            temp = list_of_integers[i]
        if (i == 1 and
        list_of_integers[i] >= list_of_integers[i + 1] and
        list_of_integers[i] >= list_of_integers[i - 1]):
            temp = list_of_integers[i]
        if i > 1:
            j = j + (i - 1)
            if j > len(list_of_integers) - 1:
                return temp
            if (j == len(list_of_integers) - 1 and
            list_of_integers[j] >= list_of_integers[j - 1]):
                temp = list_of_integers[j]
            if (j == len(list_of_integers) - 1 and
            list_of_integers[j] <= list_of_integers[j - 1]):
                temp = list_of_integers[j - 1]
            if (j < len(list_of_integers) - 1 and
            j != len(list_of_integers) - 1):
                if (list_of_integers[j] >= list_of_integers[j + 1] and
                list_of_integers[j] >= list_of_integers[j - 1]):
                    temp = list_of_integers[j]

    return temp
