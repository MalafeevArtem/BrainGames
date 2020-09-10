"""Game logic module."""
from brain_games.random_number import random_generator
from brain_games.index import play_game


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """
    Check the evenness of the number.

    Args:
        number (int): Random number.

    Returns:
        bool
    """
    return number % 2 == 0


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    number = random_generator()
    question = 'Question: {0}'.format(number)
    true_answer = 'yes' if is_even(number) else 'no'
    game_data = [question, true_answer]

    return game_data


play_game(DESCRIPTION, get_game_data)
