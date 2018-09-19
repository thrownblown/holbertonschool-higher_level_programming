#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        aa = 0
    else:
        aa = tuple_a[0]
    if len(tuple_b) == 0:
        aa += 0
    else:
        aa += tuple_b[0]

    if len(tuple_a) > 1:
        bb = tuple_a[1]
    else:
        bb = 0
    if len(tuple_b) > 1:
        bb += tuple_b[1]
    else:
        bb += 0
    return (aa, bb)
