"""Game logic module."""
from brain_games.random_number import random_generator
from brain_games.index import play_game
from random import choice


description = 'What number is missing in the progression?'
length_progression = 10


def create_progression(length, step):
    start_value = random_generator()
    progression = [start_value]
    length -= 1

    while length:
      start_value += step
      progression.append(start_value)
      length -= 1

    return progression


def create_question(progression, empty):
    question = []

    for i in progression:
      if (i == empty):
        question.append('..')
      else:
        question.append(str(i))

    return ' '.join(question)

def get_game_data():
    step = random_generator(1, length_progression - 1)
    progression = create_progression(length_progression, step)
    true_answer = choice(progression)
    question = create_question(progression, true_answer)

    game_data = [question, str(true_answer)]

    return game_data


play_game(description, get_game_data)