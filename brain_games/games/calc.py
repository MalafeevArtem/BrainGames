"""Game logic module."""
import random
import operator


DESCRIPTION = 'What is the result of the expression?'
OPERATIONS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def get_game_data():
    """
    Collect game data.

    Returns:
        DESCRIPTION (str): Game rules.
        data (list): Сontains a question and an answer.
    """
    operation, calculate = random.choice(OPERATIONS)
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    true_answer = str(calculate(operand1, operand2))

    return ('{0} {1} {2}'.format(operand1, operation, operand2), true_answer)
