#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

        Returns:
            bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Helper function to check if a byte is a valid leading byte
    def is_valid_leading_byte(byte):
        return (byte & 0b10000000) == 0b00000000 or (
                byte & 0b11100000) == 0b11000000 or (
                        byte & 0b11110000) == 0b11100000 or (
                                byte & 0b11111000) == 0b11110000

    # Helper function to check if a byte is a valid following byte
    def is_valid_following_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    # Initialize count to keep track of remaining bytes for a character
    count = 0

    for byte in data:
        if count == 0:
            if (byte & 0b10000000) == 0b00000000:
                # Single-byte character
                continue
            elif (byte & 0b11100000) == 0b11000000:
                # Two-byte character
                count = 1
            elif (byte & 0b11110000) == 0b11100000:
                # Three-byte character
                count = 2
            elif (byte & 0b11111000) == 0b11110000:
                # Four-byte character
                count = 3
            else:
                # Invalid leading byte
                return False
        else:
            if not is_valid_following_byte(byte):
                # Invalid following byte
                return False
            count -= 1

    # If there are remaining bytes, it's an incomplete character
    return count == 0
