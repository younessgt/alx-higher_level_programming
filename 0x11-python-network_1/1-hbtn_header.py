#!/usr/bin/python3
""" python script that send a request and display the value
of the X-Request-Id variable found in the header of the response"""

from urllib.request import urlopen
from sys import argv
if __name__ == "__main__":

    with urlopen(argv[1]) as response:
        resp_heads = response.headers
    result = resp_heads.get('X-Request-Id')
    print(result)
