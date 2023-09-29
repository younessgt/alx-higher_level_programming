#!/usr/bin/python3
""" this script send a post request the the url with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    value = argv[2]

    res = requests.post(url, data={'email': value})
    print(res.text)
