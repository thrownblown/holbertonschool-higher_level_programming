#!/usr/bin/python3

def uppercase(str):
    pr_str = ""
    for i in str:
        if i >= 'a' and i <= 'z' :
            pr_str += chr(ord(i) - 32)
        else:
            pr_str += i
    print(pr_str)
