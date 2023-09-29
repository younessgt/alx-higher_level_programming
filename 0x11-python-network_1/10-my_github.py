#!/usr/bin/python3
""" script that takes your GitHub username and password and uses
the GitHub API to display your id """

from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    ur = "https://api.github.com/user"

    res = requests.get(ur, auth=(username, passwd))
    json_dict = res.json()
    print(json_dict.get("id"))
