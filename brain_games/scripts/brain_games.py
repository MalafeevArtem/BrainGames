#!/usr/bin/env python3

"""The module contains the function of greeting the user."""

from brain_games.cli import welcome_user


def greet():
    """Greet user."""
    print('Welcome to the Brain Games!')


def main():
    """Run the project code."""
    greet()
    print(welcome_user())


if __name__ == '__main__':
    main()
