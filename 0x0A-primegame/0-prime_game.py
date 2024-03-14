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

    def sieve_of_eratosthenes(n):
        """
        Generates all prime numbers up to a given number using the Sieve of
        Eratosthenes algorithm.

        Args:
            n (int): The upper limit for generating prime numbers.

        Returns:
            list: A list of prime numbers up to and including n.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

    def canWin(n):
        """
        Determines the winner of the Prime Game for a specific round.

        Args:
            n (int): The upper limit of the range for the round.

        Returns:
            str: The name of the player who wins the round.
        """
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 1:
            return "Maria"
        else:
            return "Ben"

    winners = [canWin(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
