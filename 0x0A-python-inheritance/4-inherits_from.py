#!/usr/bin/python3
""" inherits_from function module """


def inherits_from(obj, a_class):
    """ returns true if same class parents """
    return(issubclass(obj, a_class))
