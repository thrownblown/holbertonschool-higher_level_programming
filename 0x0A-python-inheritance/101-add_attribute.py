#!/usr/bin/python3
''' add_sttribute function module '''


def add_attribute(obj, att, val):
    ''' atttempts to set attribute if possible '''
    setattr(obj, att, val)
    if not hasattr(obj, att):
        raise TypeError("can't add new attribute")
