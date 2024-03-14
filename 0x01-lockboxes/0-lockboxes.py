#!/bin/usr/python3
"""
You have n number of locked boxes in front of you
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    if not boxes:
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
