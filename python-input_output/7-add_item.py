#!/usr/bin/python3

"""
A script that adds all arguments to a Python list,
and then save them to a file
"""
from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


json_file_name = "add_item.json"
try:
    json_list = load_from_json_file(json_file_name)
except FileNotFoundError:
    json_list = []

for k in range(1, len(argv)):
    json_list.append(argv[k])

save_to_json_file(json_list, json_file_name)
