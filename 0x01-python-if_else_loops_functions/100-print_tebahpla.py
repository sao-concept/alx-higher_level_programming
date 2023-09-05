#!/usr/bin/python3
# Loop through ASCII values for lowercase letters 'z' to 'a' in reverse order.
for i in range(ord('z'), ord('a') - 1, -1):
    # Calculate the difference to adjust the ASCII value based on parity.
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    # Print the character adjusted by the difference without a newline.
    print('{}'.format(chr(i - diff)), end='')

# This code prints alternating lowercase letters from 'z' to 'a'.
