#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return([a if a is not search else replace for a in my_list])
