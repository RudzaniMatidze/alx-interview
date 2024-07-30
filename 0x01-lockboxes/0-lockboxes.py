#!/usr/bin/python3
"""
 a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each element
        is a list of keys available in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    # BFS-like traversal using the keys queue
    while keys:
        current = keys.pop(0)
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    # Check if all boxes have been unlocked
    return all(unlocked)
