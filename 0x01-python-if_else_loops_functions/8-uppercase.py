#!/usr/bin/python3
def uppercase(str):
    sum = ""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
            sum += c
        else:
            sum += c
    print(sum)
