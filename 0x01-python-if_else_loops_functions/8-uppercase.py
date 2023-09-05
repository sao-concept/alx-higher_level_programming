#!/usr/bin/python3
def uppercase(input_str):
    """
    Convert lowercase letters in a string to uppercase.

    Args:
        input_str (str): The input string to convert.

    Returns:
        str: The input string with lowercase letters converted to uppercase.
    """
    result = ""
    for char in input_str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Example usage:
# result = uppercase("Hello World")  # Returns "HELLO WORLD"
