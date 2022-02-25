"""Command line interface for brain-games."""

import prompt


def print_text(text: str) -> None:
    """
    Print text into command line interface.

    Args:
        text: text for print
    """
    print(text)


def welcome_user() -> str:
    """
    Ask and return user name.

    Returns:
        str
    """
    print_text('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print_text('Hello, {name}!'.format(name=name))
    return name


def ask(question: str) -> str:
    """
    Ask question and return user's answer.

    Args:
        question: question for user

    Returns:
        str

    """
    print_text('Question: {0}'.format(question))
    return prompt.string('Your answer: ', empty=True)
