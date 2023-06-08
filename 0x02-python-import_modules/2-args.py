#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv)
    if lenargv < 2:
        print("{} arguments.".format(lenargv))
    else:
        print("{} arguments:".format(lenargv - 1))
        for i in range(1, lenargv):
            print("{}: {}".format(i, sys.argv[i]))
