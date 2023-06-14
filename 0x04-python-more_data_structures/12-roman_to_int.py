#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    prev_val = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] not in 'IVXLCDM':
            return 0
        val= dict_roman[roman_string[i]]
        if val > prev_val:
            summ += val - 2 * prev_val
        else:
            summ += val
        prev_val = val
    return summ
