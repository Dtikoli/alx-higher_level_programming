#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    remain = number % (-10)
else:
    remain = number % 10

if remain > 5:
    print(f"Last digit of {number} is {remain} and is greater than 5")
elif remain == 0:
    print(f"Last digit of {number} is {remain} and is 0")
else:
    print(f"Last digit of {number} is {remain} and is less than 6 and not 0")
