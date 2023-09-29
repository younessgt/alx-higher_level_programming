#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
using requests package """

import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    res_text = f"""Body response:
    \t- type: {type(res.text)}
    \t- content: {res.text}"""
    print(res_text)
