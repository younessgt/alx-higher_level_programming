#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = abs(number) % 10
if number < 0:
    mod = -mod
if mod == 0:
    print(f"last digit of {number} is {mod} and is 0")
elif mod > 5:
     print(f"last digit of {number} is {mod} and is greater than 5 an not 0")
else:
    print(f"last digit o {number} is {mod} and is less than 6 and not 0")
