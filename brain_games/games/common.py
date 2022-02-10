"""Common functions and settings for all games."""

from random import randint
from typing import Callable

from brain_games.cli import print_text, welcome_user

RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 100
ROUNDS = 3


def run_game(welcome_message: str, build_question: Callable, ask_question: Callable) -> None:
    """
    Engine for all games.

    This function implements common logic for any game.

    Args:
        welcome_message: message is displayed at the beginning of the game
        build_question: function to prepare question and right answer
        ask_question: function to ask question to user
    """
    name = welcome_user()
    print_text(welcome_message)

    for _ in range(ROUNDS):
        question, right_answer = build_question()

        answer = ask_question(question)
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)


def check_answer(answer: str, right_answer: str, user_name: str) -> bool:
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
    print_text("Let's try again, {s1}!".format(s1=user_name))
    return False


def congratulate_user(user_name: str) -> None:
    """
    Print to user congratulations.

    Args:
        user_name: user's name
    """
    print_text('Congratulations, {name}!'.format(name=user_name))


def calc_gcd(number1: int, number2: int) -> int:
    """
    Calulate greatest common devizor.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    min_num = min(number1, number2)
    gcd = 1
    for candidate in range(2, min_num + 1):
        if number1 % candidate == 0 and number2 % candidate == 0:
            gcd = candidate

    return gcd


def random_int() -> int:
    """Return random integer.

    Returns:
        int
    """
    return randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
