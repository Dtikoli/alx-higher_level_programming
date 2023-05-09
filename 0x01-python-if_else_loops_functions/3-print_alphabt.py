#!/usr/bin/python3
for ch in range(ord('a'), ord('z')+1):
    if chr(ch) != 'q' and chr(ch) != 'e':
        print("{:c}".format(ch), end='')
