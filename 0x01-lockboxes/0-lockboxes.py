#!/usr/bin/python3
"""
Module for checking if all lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box
            and contains keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    # Initialize a set to keep track of the boxes that can be opened
    unlocked_boxes = {0}

    # Use a stack to keep track of the keys we have and explore the boxes
    stack = [0]

    while stack:
        current_box = stack.pop()
        current_keys = boxes[current_box]

        for key in current_keys:
            if key not in unlocked_boxes and 0 <= key < len(boxes):
                # Add the key to the set of unlocked boxes
                unlocked_boxes.add(key)
                # Add the key to the stack to explore its box later
                stack.append(key)

    # Check if all boxes can be opened
    return len(unlocked_boxes) == len(boxes)
