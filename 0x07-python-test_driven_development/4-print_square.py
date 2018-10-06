#!/usr/bin/python3
def check_types(err, type_list, *argv):
    ''' if none throws a different err msg, do a separate none check '''
    for i in argv:
        if i is None:
            raise TypeError(err)
        t = type(i)
        if t not in type_list:
            raise TypeError(err)
    return (True)


def print_square(size):
    check_types("size must be an integer", [int], size)
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print('#', end='')
        print('')