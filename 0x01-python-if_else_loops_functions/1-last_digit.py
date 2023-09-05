#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000 (inclusive).
number = random.randint(-10000, 10000)

# Determine the last digit of the random number.
if number < 0:
    last_digit = number % -10  # Calculate the last digit for negative numbers.
else:
    last_digit = number % 10   # Calculate the last digit for positive numbers.

# Check if the last digit is greater than 5.
if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
# Check if the last digit is less than 6 and not equal to 0.
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
# If the last digit is 0, handle it as a special case.
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
