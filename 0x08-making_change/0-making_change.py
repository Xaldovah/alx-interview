#!/usr/bin/python3
"""Module for making change"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of the values of the coins in possession.
        total (int): The target amount total to make using the coins.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, returns 0.
             If total cannot be met by any number of coins you have, returns -1.

    Note:
        - The value of a coin will always be an integer greater than 0.
        - You can assume you have an infinite number of each denomination of coin in the list.
        - This solution's runtime will be evaluated in this task.
    """
    if total < 0:
        return 0
    if total == 0:
        return 0
    
    # Initialize an array to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update dp[i] if using that coin results in a smaller number of coins
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the fewest number of coins needed to make the total amount
    return dp[total] if dp[total] != float('inf') else -1
