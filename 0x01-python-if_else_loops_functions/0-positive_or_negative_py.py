#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive", number)
else if number < 0:
    print("{} is negative", number)
else:
    pritn("{} is zero", number)
