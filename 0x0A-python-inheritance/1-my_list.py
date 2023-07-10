#!/usr/bin/python3
""" Module containing MyList class"""


class MyList(list):
    """ The class is created"""

    def print_sorted(self):
        """function that prints a sorted list"""

        ls = []
        for i in self:
            ls.append(i)
        ls.sort()
        print(ls)
