#!/usr/bin/python3
def no_c(my_string):
    retval = u""
    for char in my_string:
        if char != u'c' and char != u'C':
            retval += char
    return(retval)
