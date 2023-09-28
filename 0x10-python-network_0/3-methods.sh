#!/bin/bash
#  Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
