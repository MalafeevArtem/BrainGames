"""Game logic module."""
from brain_games.index import play_game

import math
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """
    Сheck if it is a prime number.

    Args:
        number (int): Random value.

    Returns:
        bool: Prime or not.
    """
    if number < 2:
        return False
    elif number == 2:
        return True

    divider = 2
    limit = int(math.sqrt(number))

    while divider <= limit:
        if number % divider == 0:
            return False
        divider += 1

    return True


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    number = random.randint(1, 100)
    true_answer = 'yes' if is_prime(number) else 'no'
    
    return (number, true_answer)
