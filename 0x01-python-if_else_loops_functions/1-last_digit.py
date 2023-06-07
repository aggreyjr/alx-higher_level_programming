#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = str(number)[-1:]
b = str(number)[:1]
if number > 0:
    if int(a) > 5:
        print(f"Last digit of {number} is {a} and is greater than 5")
    elif int(a) == 0:
        print(f"Last digit of {number} is {a} and is 0")
    elif int(a) <= 5 & int(a) != 0:
        print(f"Last digit of {number} is {a} and is less than 6 and not 0")
elif number < 0:
    c = b + a
    if int(c) == 0:
        print(f"Last digit of {number} is {a} and is 0")
    else:
        print(f"Last digit of {number} is {c} and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number} is {number} and is 0")
