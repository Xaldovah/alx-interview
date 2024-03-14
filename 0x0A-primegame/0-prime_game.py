#!/usr/bin/python3
"""
Module to determine the winner of the Prime Game
"""


def sieve(n):
    """
    Generates all prime numbers up to a given number using the Sieve of
    Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
    list: A list of prime numbers up to and including n.
    """
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes


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
    maria_wins = ben_wins = 0

    for n in nums:
        primes = sieve(n)
        remaining = set(range(1, n + 1))

        turn = "Maria"
        while remaining:
            available_primes = [p for p in primes if p in remaining]
            if not available_primes:
                break
            chosen_prime = max(
                    available_primes) if turn == "Maria" else min(
                            available_primes)
            remaining -= set(range(chosen_prime, n + 1, chosen_prime))
            turn = "Ben" if turn == "Maria" else "Maria"

        if turn == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
