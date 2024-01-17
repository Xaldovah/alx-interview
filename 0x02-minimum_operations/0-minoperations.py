#!/usr/bin/python3
"""
Minimum Operations Module
"""


def minOperations(n):
    """
    This calculates the fewest number of operations needed to result
    in exactly n H characters in a file where there is a single character H
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
