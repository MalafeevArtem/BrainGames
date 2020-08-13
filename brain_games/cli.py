"""The module contains a prompt string."""

import prompt


def welcome_user():
    """
    Greet the user.

    Returns:
        str
    """
    name_user = prompt.string('\nMay I have your name? ')
    return 'Hello, {0}!'.format(name_user)
