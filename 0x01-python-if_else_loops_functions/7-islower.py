#!/usr/bin/python3
for i in range(97, 123):
    print("{}".format(chr(i)), end='')

def islower(c):
    c = ord(c)
    if c > 96 and c < 124:
        return True
    return False
