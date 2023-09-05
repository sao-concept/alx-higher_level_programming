#!/usr/bin/python3
def islower(c):
    """
    Check if a character is a lowercase letter.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if the character is a lowercase letter, False otherwise.
    """
    return 97 <= ord(c) <= 122

# Example usage:
# result = islower('a')  # Returns True
# result = islower('A')  # Returns False
