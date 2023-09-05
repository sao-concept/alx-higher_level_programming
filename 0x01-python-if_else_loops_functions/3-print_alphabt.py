#!/usr/bin/python3
# Loop through ASCII values for lowercase letters 'a' to 'z'.
for ascii_value in range(ord('a'), ord('z') + 1):
    # Check if the character is not 'e' or 'q'.
    if chr(ascii_value) != 'e' and chr(ascii_value) != 'q':
        # Convert ASCII to character and print without a newline.
        print('{:c}'.format(ascii_value), end='')

# This code prints all lowercase letters from 'a' to 'z', excluding
# 'e' & 'q'.
