#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        for item in my_list:
            if idx < x:
                print(item, end='')
                idx += 1
            else:
                break
        print("")
        return (idx)
    except TypeError:
        return (0)
