#!/usr/bin/python3

"""
A script that adds all arguments to a Python list,
and then save them to a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


json_file_name = "add_item.json"
try:
    jsonlist = load_from_json_file(json_file_name)
except FileNotFoundError:
    jsonlist = []

for k in range(1, len(argv)):
    jsonlist.append(argv[k])

save_to_json_file(jsonlist, json_file_name)
