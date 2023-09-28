#!/bin/bash
# script that send a GET request including a custom HTTP header in the request
curl -s -H "X-School-User-Id: 98" "$1"
