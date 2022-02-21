"""Common functions and settings for all games."""

from random import randint
from typing import Callable

import prompt

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
    print(welcome_message)

    for _ in range(ROUNDS):
        question, right_answer = build_question()

        answer = ask_question(question)
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)


def welcome_user() -> str:
    """
    Ask and return user name.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
    return name


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
        print('Correct!')
        return True

    template = "'{s1}' is wrong answer ;(. Correct answer was '{s2}'."
    print(template.format(s1=answer, s2=right_answer))
    print("Let's try again, {s1}!".format(s1=user_name))
    return False


def congratulate_user(user_name: str) -> None:
    """
    Print to user congratulations.

    Args:
        user_name: user's name
    """
    print('Congratulations, {name}!'.format(name=user_name))


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
    max_candidate = min_num // 2 + 1
    gcd = 1
    for candidate in range(2, max_candidate):
        if number1 % candidate == 0 and number2 % candidate == 0:
            gcd = candidate

    return gcd


def random_int() -> int:
    """Return random integer.

    Returns:
        int
    """
    return randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)


def answer_yes_no(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers: 'yes' and 'no', otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print(question)
    answer = prompt.string('Your answer: ')
    while answer not in {'yes', 'no'}:
        answer = prompt.string('Answer "yes" or "no". Your answer: ')
    return answer


def answer_int(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers is correct integer, otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print(question)
    return str(prompt.integer('Your answer: ', empty=False))
