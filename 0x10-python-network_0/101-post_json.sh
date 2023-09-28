#!/bin/bash
# Script that send a Json Post request  (the data to send is  in "my_json_0 file")
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
