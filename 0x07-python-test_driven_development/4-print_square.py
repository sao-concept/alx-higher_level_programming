#!/usr/bin/python3
"""
`print_square` module
This function prints a square with the character #
"""


def print_square(size):
    """prints a square with size, `size`
    Args:
        size (int)
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size)
