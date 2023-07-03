#!/usr/bin/python3
"""
This module contain a function called text_indentation
function:
    text_indentation: function that print 2 new line after ":" or
    "?" or "."
"""


def text_indentation(text):
    """
    defining the function
    """
    sentence = ""
    if type(text) != str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter in [".", ":", "?"]:
            sentence += letter + "\n"
        else:
            sentence += letter
    lists = sentence.strip().splitlines()
    for i in range(len(lists)):
        if i < len(lists) - 1:
            print(lists[i].strip())
            print("")
        else:
            print(lists[i].strip(), end="")
