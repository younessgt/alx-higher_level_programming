#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        f = int(i % 3)
        b = int(i % 5)
        if f == 0 and b != 0:
            print("Fizz ", end="")
        if b == 0 and f != 0:
            print("Buzz ", end="")
        if f == 0 and b == 0:
            print("FizzBuzz ", end="")
        if f != 0 and b != 0:
            print("{} ".format(i), end="")
