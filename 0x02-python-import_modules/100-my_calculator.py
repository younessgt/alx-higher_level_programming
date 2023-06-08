#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    
    if len(argv) -1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    argv[1] = int(argv[1])
    argv[3] = int(argv[3])

    if argv[2] == "+":
        c = add(argv[1], argv[3])
        print("{} + {} = {}".format(argv[1], argv[3], c))
        exit(0)
    elif argv[2] == "-":
        c = sub(argv[1], argv[3])
        print("{} - {} = {}".format(argv[1], argv[3], c))
        exit(0)
    elif argv[2] == "*":
        c = mul(argv[1], argv[3])
        print("{} * {} = {}".format(argv[1], argv[3], c))
    elif argv[2] == "/":
        c = div(argv[1], argv[3])
        print("{} / {} = {}".format(argv[1], argv[3], c))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

