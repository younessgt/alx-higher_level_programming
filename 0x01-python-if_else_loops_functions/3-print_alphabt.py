#!/usr/bin/python3
for i in range(26):
    j = chr(97 + i)
    if (j != 'q') and (j != 'e'):
        print("{}".format(j), end="")
