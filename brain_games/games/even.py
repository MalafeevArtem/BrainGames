import prompt
from random import randint


def is_even(number):
    return number % 2 == 0


def random_generator():
    max_value = 100
    min_value = 1

    return randint(min_value, max_value)


def ask_name():
    return prompt.string('\nMay I have your name? ')


def start_game():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name_user = ask_name()
    print('Hello, {0}!\n'.format(name_user))
    number_of_rounds = 3

    def play(count):
        if count == 0:
            print('Congratulations, {0}'.format(name_user))
            return

        number = random_generator()
        print('Question: {0}'.format(number))
        true_answer = 'yes' if is_even(number) else 'no'
        ask_answer_user = prompt.string('Your answer: ')

        if true_answer == ask_answer_user:
            print('Correct!')
            play(count - 1)
        else:
            print('"{0}" is wrong answer ;(. Correct answer was "{1}"'.format(ask_answer_user, true_answer))
            print('Let\'s try again, {0}!'.format(name_user))

    play(number_of_rounds)
