"""The module contains a function for generating a random number."""
from random import randint


def random_generator():
    """
    Return a random number in a given range.

    Returns:
        int: random number
    """
    max_value = 100
    min_value = 1

    return randint(min_value, max_value)
