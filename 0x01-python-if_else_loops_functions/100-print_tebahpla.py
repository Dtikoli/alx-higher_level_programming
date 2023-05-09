#!/usr/bin/python3
for ch in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(ch) if ch % 2 == 0 else chr(ch-32), end='')
