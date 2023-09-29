#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib.request import urlopen
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        content_html = response.read()
    print("Body response:")
    print("\t- type:", type(content_html))
    print("\t- content:", content_html)
    print("\t- utf8 content:", content_html.decode('utf-8'))
