#!/usr/bin/python3
"""
Module to determine the winner of the Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list): An array of integers representing the range for each round

        Returns:
            str or None: The name of the player that won the most rounds.
            If the winner cannot be determined, returns None.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
