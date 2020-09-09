"""The module contains a function for generating a random number."""
from random import randint


def random_generator(min_value=1, max_value=100):
    """
    Return a random number in a given range.

    Args:
        max_value (int): Мaximum value of a random number.
        min_value (int): Мinimum value of a random number.

    Returns:
        int: random number
    """
    return randint(min_value, max_value)
