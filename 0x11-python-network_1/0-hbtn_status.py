#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib.request import urlopen

url = 'https://alx-intranet.hbtn.io/status'
with urlopen(url) as response:
    content_html = response.read()
body = f"""Body response:
    - type: {type(content_html)}
    - content: {content_html}
    - utf8 content: {content_html.decode('utf-8')}"""
print(body)
