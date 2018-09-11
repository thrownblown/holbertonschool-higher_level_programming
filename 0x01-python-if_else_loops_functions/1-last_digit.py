#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pr_str = "Last digit of {} is {} and is {}"
if number < 0:
    rem = (number * -1) % 10
else:
    rem = number % 10
if rem > 5:
    print(pr_str.format(number, rem, "greater than 5"))
elif rem == 0:
    print(pr_str.format(number, rem, "0"))
else:
    print(pr_str.format(number, rem, "less than 6 and not 0"))
