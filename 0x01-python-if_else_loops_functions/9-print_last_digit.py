#!/usr/bin/python3
def print_last_digit(number):
    """
    Print and return the last digit of a given number.

    Args:
        number (int): The input number.

    Returns:
        int: The absolute value of the last digit.
    """
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)

# Example usage:
# last_digit = print_last_digit(-12345)  # Prints and returns 5
