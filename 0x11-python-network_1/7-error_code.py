#!/usr/bin/python3
""" in this script we will handle the HTTP Errors using
the requests module """
from sys import argv
import requests

if __name__ == "__main__":

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
