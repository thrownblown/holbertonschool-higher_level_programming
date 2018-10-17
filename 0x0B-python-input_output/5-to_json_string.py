#!/usr/bin/python3
""" to_json_string function module """
import json.dumps as dumps


def to_json_string(my_obj):
    """ json stringifies my_obj """
    return dumps(my_obj)
