#!/usr/bin/python3
for ascii_value in range(ord('a'), ord('z') + 1):
    if chr(ascii_value) != 'e' and chr(ascii_value) != 'q':
        print('{:c}'.format(ascii_value), end='')
