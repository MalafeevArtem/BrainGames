"""Game logic module."""
import random


DESCRIPTION = 'What number is missing in the progression?'
LENGTH_PROGRESSION = 10


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    start = random.randint(1, 100)
    diff = random.randint(1, 10)
    gap = random.randint(0, 9)
    progression = []

    for index in range(LENGTH_PROGRESSION):
        number = start + diff * index

        if index == gap:
            true_answer = str(number)
            part = '..'
        else:
            part = str(number)

        progression.append(part)

    question = ' '.join(progression)

    return (question, true_answer)
