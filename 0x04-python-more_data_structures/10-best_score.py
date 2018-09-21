#!/usr/bin/python3
def best_score(a_dictionary):
    if not len(a_dictionary):
        return None
    mx = 0
    for i in a_dictionary[i]:
        if a_dictionary[i] > mx:
            mx = i
    return mx
