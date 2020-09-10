"""Game logic module."""
from brain_games.random_number import random_generator
from brain_games.index import play_game
from random import choice


DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def create_progression(length, step):
    """
    Create an arithmetic progression..

    Args:
        length (int): Length of arithmetic progression.
        step (int): The step with which the arithmetic progression increases.

    Returns:
        progression (list): Аrithmetic progression.
    """
    start_value = random_generator()
    progression = [start_value]
    length -= 1

    while length:
        start_value += step
        progression.append(start_value)
        length -= 1

    return progression


def create_question(progression, empty):
    """
    Create a question with a missing element.

    Args:
        progression (list): Аrithmetic progression.
        empty (int): Random item to skip.

    Returns:
        (str): The string that contains the program with the missing element.
    """
    question = []

    for number in progression:
        if (number == empty):
            question.append('..')
        else:
            question.append(str(number))

    return ' '.join(question)


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    step = random_generator(1, LENGTH_PROGRESSION - 1)
    progression = create_progression(LENGTH_PROGRESSION, step)
    true_answer = choice(progression)
    question = create_question(progression, true_answer)

    game_data = [question, str(true_answer)]

    return game_data


play_game(DESCRIPTION, get_game_data)
