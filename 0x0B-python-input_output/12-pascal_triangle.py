#!/usr/bin/python3
"""A module that defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    ptriangle = [[1]]
    while len(ptriangle) != n:
        triangle = ptriangle[-1]
        Tmplist = [1]
        for t in range(len(triangle) - 1):
            Tmplist.append(triangle[t] + triangle[t + 1])
        Tmplist.append(1)
        ptriangle.append(Tmplist)
    return ptriangle
