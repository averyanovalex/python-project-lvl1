"""Command line interface for brain-games."""

import prompt


def welcome_user() -> str:
    """
    Ask and return user name.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
