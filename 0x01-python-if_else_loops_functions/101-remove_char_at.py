#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0 and n < len(str):
        new = str[:n] + str[n + 1:]
    else:
        new = str
    return (new)
