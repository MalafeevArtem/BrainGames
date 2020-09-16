"""Game logic module."""
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(operand1, operand2):
    """
    Find the greatest common share.

    Args:
        operand1 (int): Random number.
        operand2 (int): Random number.

    Returns:
        int: greatest common factor.
    """
    while operand1 != 0 and operand2 != 0:
        if operand1 > operand2:
            operand1 %= operand2
        else:
            operand2 %= operand1

    return operand1 + operand2


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    true_answer = str(find_gcd(operand1, operand2))

    return ('{0} {1}'.format(operand1, operand2), true_answer)
