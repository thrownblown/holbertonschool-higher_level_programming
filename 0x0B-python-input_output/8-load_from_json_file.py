#!/usr/bin/python3
""" load_from_json_file function module """
import json


def load_from_json_file(filename):
    """ parses json file returns obj """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.readline())
