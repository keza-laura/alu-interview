#!/usr/bin/python3
"""
Module that calculates how much rainwater is trapped.
"""


def rain(walls):
    """
    Calculate how many square units of water are retained.

    Args:
        walls (list): List of non-negative integers.

    Returns:
        int: Total amount of trapped rainwater.
    """

    if not walls or len(walls) < 3:
        return 0

    left = 0
    right = len(walls) - 1

    left_max = 0
    right_max = 0

    trapped_water = 0

    while left < right:

        if walls[left] < walls[right]:

            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                trapped_water += left_max - walls[left]

            left += 1

        else:

            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                trapped_water += right_max - walls[right]

            right -= 1

    return trapped_water
