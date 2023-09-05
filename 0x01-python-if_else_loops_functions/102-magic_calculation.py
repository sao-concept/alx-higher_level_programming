#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    Perform a magic calculation based on the values of 'a', 'b', and 'c'.

    Args:
        a (int): The first input.
        b (int): The second input.
        c (int): The third input.

    Returns:
        int: The result of the magic calculation.
    """
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c

# Example usage:
# result = magic_calculation(5, 10, 3)  # Returns 15
