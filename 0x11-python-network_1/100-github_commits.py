#!/usr/bin/python3
""" Script that display the 10 most recent commits"""

from sys import argv
import requests

if __name__ == "__main__":

    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1]))
    result = res.json()
    for i in range(10):
        print("{}: {}".format(
                result[i].get("sha"),
                result[i].get("commit").get("author").get("name")))
