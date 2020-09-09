"""Game logic module."""
from brain_games.random_number import random_generator
from brain_games.index import play_game
from random import choice


description = 'What number is missing in the progression?'
length_progression = 10


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
        description (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    step = random_generator(1, length_progression - 1)
    progression = create_progression(length_progression, step)
    true_answer = choice(progression)
    question = create_question(progression, true_answer)

    game_data = [question, str(true_answer)]

    return game_data


play_game(description, get_game_data)
