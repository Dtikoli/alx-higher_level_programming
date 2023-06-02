#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0,) * 2
    b = tuple_b + (0,) * 2
    sums = tuple(i + j for i, j in zip(a, b))
    return sums[0:2]
