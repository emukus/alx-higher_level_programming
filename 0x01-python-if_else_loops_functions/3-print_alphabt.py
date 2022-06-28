#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i != 'e' and i != 'q':
        print("{:c}".format(i), end='')
