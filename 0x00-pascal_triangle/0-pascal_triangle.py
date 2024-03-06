#!/usr/bin/python3
"""Pascal Triangle Interview"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        R = [0] * (i + 1)
        R[0] = 1
        R[len(R) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(R):
                x = pascal_triangle[i - 1][j - 1]
                y = pascal_triangle[i - 1][j]
                R[j] = x + y

        pascal_triangle[i] = R

    return pascal_triangle
