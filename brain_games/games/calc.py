"""Game logic module."""
from brain_games.random_number import random_generator
from brain_games.index import play_game

import random


DESCRIPTION = 'What is the result of the expression?'
operations = ['+', '-', '*']


def calculate_result(operation, operand1, operand2):
    """
    Evaluate the expression.

    Args:
        operation (str): random operator
        operand1 (int): first value
        operand2 (int): second value

    Returns:
        int: calculation result
    """
    if operation == '+':
        return operand1 + operand2
    elif operation == '-':
        return operand1 - operand2

    return operand1 * operand2


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    operation = random.choice(operations)
    operand1 = random_generator()
    operand2 = random_generator()
    question = 'Question: {0} {1} {2}'.format(operand1, operation, operand2)
    true_answer = str(calculate_result(operation, operand1, operand2))
    game_data = [question, true_answer]

    return game_data


play_game(DESCRIPTION, get_game_data)
