#!/usr/bin/python3
"""
In a text file, there is a single character H
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

Example:

n = 9
H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n (iterations)
    H (operations)
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterations = 2
    while (iterations <= n):
        iterations += 1
        if (n % iterations == 0):
            operations += iterations
            n //= iterations  # update n
            iterations = 1  # stop loop to start calcul to new updated n
    return operations
