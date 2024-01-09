# Lockboxes

## Overview

This Python script provides a method to determine if all lockboxes can be opened. Each box contains keys to other boxes, and the goal is to check if it's possible to unlock all boxes, starting from the initially unlocked box.

## Method

The `canUnlockAll` method takes a list of lists as input, where each inner list represents a box and contains keys to other boxes. The method employs a depth-first search algorithm to explore the boxes and checks if all boxes can be opened.

## Usage

```python
#!/usr/bin/python3

from lockboxes import canUnlockAll

# Example usage
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
