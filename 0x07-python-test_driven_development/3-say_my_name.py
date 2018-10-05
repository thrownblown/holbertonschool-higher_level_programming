#!/usr/bin/python3
def check_types(err, type_list, *argv):
    for i in argv:
        if i is None:
            raise TypeError(err)
        t = type(i)
        if t not in type_list:
            raise TypeError(err)
    return (True)


def say_my_name(first_name, last_name=""):
    check_types("first_name must be a string", [str], first_name)
    check_types("last_name must be a string", [str], last_name)
    print("My name is {:s} {:s}".format(first_name, last_name))
