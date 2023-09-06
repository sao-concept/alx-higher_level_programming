#!/usr/bin/python3
# Loop through ASCII values for lowercase letters 'a' to 'z'.
for ascii_value in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(ascii_value), end='')
# This code prints all lowercase letters from 'a' to 'z' without a newline.
