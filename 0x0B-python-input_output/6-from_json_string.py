#!/usr/bin/python3
""" from_json_string function module """
import json


def from_json_string(my_str):
    """ json parses my_str """
    return json.loads(my_str)
