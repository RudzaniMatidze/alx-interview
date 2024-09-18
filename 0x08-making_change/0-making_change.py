#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    # sort coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        change += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return change
