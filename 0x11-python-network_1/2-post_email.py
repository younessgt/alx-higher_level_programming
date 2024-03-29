#!/usr/bin/python3
""" this script send a post request the the url with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = argv[2]

    temp = {}
    temp['email'] = value

    data_to_send = urlencode(temp)
    data_to_send = data_to_send.encode('ascii')
    req = Request(url, data_to_send)
    with urlopen(req) as response:
        content = response.read()
    print(content.decode('utf-8'))
