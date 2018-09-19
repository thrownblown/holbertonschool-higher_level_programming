#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng:
       return (leng, sentence[0])
    return (0, None)
