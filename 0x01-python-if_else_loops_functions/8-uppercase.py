#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(c) - (ord('a') - ord('A')))
        print("{:s}".format(i), end='')
    print("")
