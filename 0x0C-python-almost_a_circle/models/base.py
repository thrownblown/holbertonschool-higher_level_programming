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
        """ returns a json string of supplied dict """
        if not list_dictionaries:
            return ("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json to file"""
        filename = str(cls.__name__) + '.json'
        with open(filename, 'w+', encoding='utf-8') as json_file:
            json_file.seek(0)
            obj_list = []
            if len(list_objs):
                for obj in list_objs:
                    obj_list.append(obj.to_dictionary())
            json_file.write(Base.to_json_string(obj_list))
