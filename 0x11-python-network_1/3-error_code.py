#!/usr/bin/python3
""" in this script we will handle the HTTP Errors using
the urllib.error module """

from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError
if __name__ == "__main__":
    url = argv[1]

    try:
        with urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
