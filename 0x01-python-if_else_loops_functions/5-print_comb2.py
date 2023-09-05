#!/usr/bin/python3
# Loop through numbers from 0 to 98 (99 exclusive).
for num in range(99):
    # Print the number with leading zeros and a comma, except
    # for the last number.
    print('{:02d}, '.format(num), end='')

# Print the last number (99) without a comma.
print('99')

# This code prints numbers from 00 to 99 separated by commas.
