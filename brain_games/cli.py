"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """
    Ask and return user name.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


def print_text(text: str):
    """
    Print text into command line interface.

    Args:
        text: text for print
    """
    print(text)


def answer_yes_no():
    """
    Ask user and return user's answer.

    Correct answers: 'yes' and 'no', otherwise ask user again.

    Returns:
        str
    """
    answer = prompt.string('Your answer: ')
    while answer not in {'yes', 'no'}:
        answer = prompt.string('Answer "yes" or "no". Your answer: ')
    return answer
