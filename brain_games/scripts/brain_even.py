#!/usr/bin/env python3

"""The module contains the function of start the game."""

from brain_games.index import play_game
from brain_games.games import even


def main():
    """Start the game code."""
    play_game(even)


if __name__ == '__main__':
    main()
