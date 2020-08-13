import prompt

def welcome_user():
    name_user = prompt.string('\nMay I have your name? ')
    print('Hello, %s!' % name_user)