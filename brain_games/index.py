"""The module contains a prompt."""
import prompt


def play_game(game):
    """
    Launch the game interface.

    Args:
        game: Contains game data.
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name_user = prompt.string('\nMay I have your name? ')
    print('Hello, {0}!\n'.format(name_user))
    rounds_count = 3

    while rounds_count:
        (question, true_answer) = game.get_game_data()
        print('Question: {0}'.format(question))
        answer_user = prompt.string('Your answer: ')

        if (answer_user == true_answer):
            print('Correct!')
            rounds_count -= 1
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(answer_user, true_answer))
            print("Let's try again, {0}!".format(name_user))
            return

    print('Congratulations, {0}!'.format(name_user))
