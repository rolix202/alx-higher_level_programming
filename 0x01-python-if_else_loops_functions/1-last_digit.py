#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

if last_digit > 5:
    print(f"The last digit of {number:d} is {last_digit} and its greater than 5")
elif last_digit == 0:
    print(f"The last digit of {number:d} is {last_digit} and is 0")
else:
    print(f"The last digit if {number:d} is less than 6 and not 0")
