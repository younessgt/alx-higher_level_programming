#!/usr/bin/python3
""" script that add argument to python list
and save them to a file"""

from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
file_path = os.path.join(os.getcwd(), filename)
if len(argv) == 1:
    if not os.path.isfile(file_path):
        save_to_json_file([], filename)
else:
    if not os.path.isfile(file_path):
        with open(filename, 'w') as wf:
            wf.write("[]")
    load = load_from_json_file(filename)
    for i in range(1, len(argv)):
        load.append(argv[i])
    save_to_json_file(load, filename)

# without using os module we can just use try to check if the file exist
# and except load = []
