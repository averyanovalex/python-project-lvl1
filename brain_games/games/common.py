"""Common functions and settings for all games."""

from random import randint

from brain_games.cli import print_text

RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 100
ROUNDS = 3


def random_int():
    """Return random integer.

    Returns:
        int
    """
    return randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)


def check_answer(answer: str, right_answer: str, user_name: str):
    """
    Check correct users's answer or not.

    After checking, print message for user and return result.
    If user's answer is correct return True, otherwise  False.

    Args:
        answer: user's answer
        right_answer: correct answer
        user_name: user's name

    Returns:
        bool
    """
    if answer == right_answer:
        print_text('Correct!')
        return True

    template = "'{s1}' is wrong answer ;(. Correct answer was '{s2}'."
    print_text(template.format(s1=answer, s2=right_answer))
    print_text("Let's try again, {s1}".format(s1=user_name))
    return False


def congratulate_user(user_name: str):
    """
    Print to user congratulations.

    Args:
        user_name: user's name
    """
    print_text('Congratilations, {name}!'.format(name=user_name))
