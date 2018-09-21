#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret_dict = {}
    for a in a_dictionary:
        ret_dict[a] = a_dictionary[a] * 2
    return(ret_dict)
