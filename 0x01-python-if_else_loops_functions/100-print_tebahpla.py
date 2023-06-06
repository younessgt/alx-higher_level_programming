#!/usr/bin/python3
j = ord('z')
k = j
for i in range(26):
    print("{}".format(chr(k)), end="")
    if 97 <= k <= 122:
        k = j - 33
        j = j - 2
    else:
        k = j
