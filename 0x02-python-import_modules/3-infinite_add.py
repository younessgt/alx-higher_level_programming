#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0")
    else:
        summ = 0
        for i in range(1, len(argv)):
            summ += int(argv[i])
        print("{}".format(summ))
