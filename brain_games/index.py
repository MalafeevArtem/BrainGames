"""The module contains a prompt."""
import prompt


def ask_name():
    """
    Аsk username.

    Returns:
        str
    """
    return prompt.string('\nMay I have your name? ')


def play_game(description, game_data):
    """
    Launch the game interface.

    Args:
        description (str): Сontains a description of the selected game.
        game_data: Contains a question and an answer to the problem.
    """
    print('Welcome to the Brain Games!')
    print(description)
    name_user = ask_name()
    print('Hello, {0}!\n'.format(name_user))
    number_of_rounds = 3

    def play_round(count):
        if count == 0:
            print('Congratulations, {0}!'.format(name_user))
            return

        [question, true_answer] = game_data()
        print(question)
        ask_answer_user = prompt.string('Your answer: ')

        if (ask_answer_user == true_answer):
            print('Correct')
            play_round(count - 1)
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(ask_answer_user, true_answer))
            print("Let's try again, {0}!".format(name_user))

    play_round(number_of_rounds)
