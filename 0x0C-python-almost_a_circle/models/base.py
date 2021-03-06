#!/usr/bin/python3
"""Module with the Base class"""
import json
import os
import csv


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
        if not list_dictionaries or not len(list_dictionaries):
            return ("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json to file"""
        filename = str(cls.__name__) + '.json'
        with open(filename, 'w+', encoding='utf-8') as json_file:
            obj_list = []
            if list_objs and len(list_objs):
                for obj in list_objs:
                    obj_list.append(obj.to_dictionary())
            json_file.write(Base.to_json_string(obj_list))
            json_file.close()

    @staticmethod
    def from_json_string(json_string):
        """ returns object from json data string """
        if not json_string:
            json_string = "[]"
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ makes obj from dict """
        inst = cls()
        if type(dictionary) == dict:
            inst.update(**dictionary)
        return(inst)

    @classmethod
    def load_from_file(cls):
        """ loads objs json file """
        filename = str(cls.__name__) + ".json"
        obj_list = []
        if not os.path.exists(filename):
            return(obj_list)
        with open(filename, 'r+', encoding='utf-8') as json_file:
            dict_list = Base.from_json_string(json_file.read())
            for i in range(len(dict_list)):
                new = cls.create(**dict_list[i])
                obj_list.append(new)
            json_file.close()
            return(obj_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves shape object list to csv """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w+') as json_file:
            csvwriter = csv.writer(json_file)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    csvwriter.writerow([i.id, i.width, i.height, i.x, i.y])
                else:
                    csvwriter.writerow([i.id, i.size, i.x, i.y])
            json_file.close()

    @classmethod
    def load_from_file_csv(cls):
        """ creates objects from a csv file """
        filename = cls.__name__ + '.csv'
        obj_list = []
        with open(filename, 'r+') as csv_file:
            for line in csv.reader(csv_file):
                obj = cls.create()
                obj = map(int, line)
                obj.update(*list(obj))
                obj_list.append(obj)
            csv_file.close()
        return(obj_list)
