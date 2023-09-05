#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = '-' + str(number)[-1]
else:
    digit = str(number)[-1]
message = f"Last digit of {number} is {digit}"
if int(digit) > 5:
    print(message, "and is greater than 5")
elif int(digit) != 0 and int(digit) < 6:
    print(message, "and is less than 6 and not 0")
else:
    print(message, "and is 0")
