#!/usr/bin/python3
""" appends args to list, and writes list to file """
from sys import argv
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        list_from_file = load("add_item.json")
        list_from_file.extend([e for e in argv[1:]])
    except FileNotFoundError:
        list_from_file = [e for e in argv[1:]]
    finally:
        save(list_from_file, "add_item.json")
