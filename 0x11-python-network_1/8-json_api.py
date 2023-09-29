#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter """
from sys import argv
import requests

if __name__ == "__main__":

    ur = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        value = ""
    else:
        value = argv[1]
    res = requests.post(ur, data={'q': value})
    try:
        data = res.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
