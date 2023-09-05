#!/usr/bin/python3
def fizzbuzz():
    """
    Print the FizzBuzz sequence for numbers from 1 to 100.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")

# Example usage:
# fizzbuzz()  # Prints the FizzBuzz sequence from 1 to 100
