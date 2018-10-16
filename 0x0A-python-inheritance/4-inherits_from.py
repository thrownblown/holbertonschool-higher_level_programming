#!/usr/bin/python3
""" inherits_from function module """


def inherits_from(obj, a_class):
    """ returns true if same class parents """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
