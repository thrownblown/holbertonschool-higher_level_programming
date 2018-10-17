#!/usr/bin/python3
""" save_to_json_file function module """
import json


def save_to_json_file(my_obj, filename):
    """ stringifies my_obj and writes to filename """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))