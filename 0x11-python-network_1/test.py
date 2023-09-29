#!/usr/bin/python3

import urllib.request
# with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
# html = response.read()
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    print(type(response))
    html = response.read()
print(html.decode('utf-8'))
print(type(html))
