#!/usr/bin/python3
"""Module with the Base class"""
import json


class Base:
    """Base manages id attribute in future classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initer"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base._Base__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return ("[]")
        return(json.dumps(list_dictionaries))
