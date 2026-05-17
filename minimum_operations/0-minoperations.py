#!/usr/bin/python3
"""
Module that contains the minOperations function
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to get exactly n H characters in the file.

    Args:
        n (int): target number of H characters

    Returns:
        int: minimum number of operations
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
