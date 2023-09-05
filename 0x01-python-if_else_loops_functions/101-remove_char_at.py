#!/usr/bin/python3
def remove_char_at(input_str, n):
    """
    Remove a character at a specified index from a string.

    Args:
        input_str (str): The input string.
        n (int): The index of the character to remove.

    Returns:
        str: The input string with the character at index 'n' removed.
    """
    if n < 0:
        return input_str
    return input_str[:n] + input_str[n+1:]

# Example usage:
# result = remove_char_at("example", 3)  # Returns "exaple"
