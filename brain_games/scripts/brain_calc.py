#!/usr/bin/env python3

"""The module contains the function of start the game."""

from brain_games.index import play_game
from brain_games.games import calc


def main():
    """Start the game code."""
    play_game(calc)


if __name__ == '__main__':
    main()
