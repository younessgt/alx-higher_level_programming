#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        div = int(i / 10)
        mod = i % 10
        print("{}{}, ".format(div, mod), end="")
