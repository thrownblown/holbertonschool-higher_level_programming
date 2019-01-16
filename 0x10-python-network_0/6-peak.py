#!/bin/python3
# finds a peak in a list of unsorted integers.


def find_peak(list_of_integers):
    leng = len(list_of_integers)
    if leng == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return(list_of_integers[0])
        return(list_of_integers[1])
    leng = leng / 2
    a = find_peak(list_of_integers[:leng])
    b = find_peak(list_of_integers[leng:])
    if a > b:
        return a
    return b
