#!/bin/bash
# script that send a GET request and display just the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
