"""Command line interface for brain-games."""

import prompt


def welcome_user():
    """Ask user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
