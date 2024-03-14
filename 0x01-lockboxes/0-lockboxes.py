#!/usr/bin/python3
"""
Solves the lock boxes puzzle
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    if not boxes or type(boxes) is not list:
        return False

    opened = [False] * len(boxes)
    opened[0] = True

    keys = [0]
    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if not opened[key] and len(boxes) > 1:
                opened[key] = True
                keys.append(key)
    return all(opened)
