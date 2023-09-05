#!/usr/bin/python3
# Loop through numbers from 0 to 9 for 'x'.
for x in range(10):
    # Loop through numbers from 'x + 1' to 9 for 'y'.
    for y in range(x + 1, 10):
        # Check if 'x' and 'y' are 8 and 9 respectively.
        if x == 8 and y == 9:
            print('89')
        else:
            # Print 'x' and 'y' with a comma, except for the last pair.
            print('{}{}, '.format(x, y), end='')

# This code prints combinations of two numbers from 01 to 89.
