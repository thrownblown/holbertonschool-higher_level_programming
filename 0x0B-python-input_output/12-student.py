#!/usr/bin/python3
""" Student class module """


class Student:
    """ Student """

    def __init__(self, first_name, last_name, age):
        """ initer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns Student dict """
        if attrs is None:
            return self.__dict__
        elif type(attrs) is list:
            obj = {}
            for key, val in self.__dict__.items():
                if key in attrs:
                    obj[key] = val
            return obj
