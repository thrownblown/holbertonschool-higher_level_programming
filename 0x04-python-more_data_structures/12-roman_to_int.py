#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_nu = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    retval = 0
    tmp = 0

    try:
        for val in roman_string[::-1]:
            if rom_nu[val] >= tmp:
                tmp = rom_nu[val]
                retval += tmp
            else:
                retval -= rom_nu[val]
    except (TypeError, ValueError, KeyError):
        retval = 0
    return(retval)
