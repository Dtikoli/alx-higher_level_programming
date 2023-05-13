#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a) + [0]*2
    b = list(tuple_b) + [0]*2
    sums = [i + j for i, j in zip(a, b)]
    return tuple(sums[0:2])
