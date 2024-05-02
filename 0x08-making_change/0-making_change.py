#!/usr/bin/python3
""" Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """ Function that give a total,
    with a minimum coins, (Greedy Method)
    total: amount to make change for.
    coins: total coins provided
    """
    coins.sort(reverse=True)
    if total <= 0:
        return 0
    min_number = 0

    for coin in coins:
        while (total - coin) >= 0:
            total -= coin
            min_number += 1
        if total == 0:
            return min_number
    else:
        return -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
