#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('1-min').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
