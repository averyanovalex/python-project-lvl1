"""Common functions and settings for all games."""

from random import randint
from typing import Any, Callable

import prompt

RANDOM_NUMBER_MIN = -10
RANDOM_NUMBER_MAX = 50
ROUNDS_COUNT = 3


def run_game(welcome_message: str, build_question: Callable, answer_type: Any) -> None:
    """
    Engine for all games.

    This function implements common logic for any game.

    Args:
        welcome_message: message is displayed at the beginning of the game
        build_question: function to prepare question and right answer
        answer_type: available type of users's answer in game
    """
    user_name = welcome_user()
    print(welcome_message)

    for _ in range(ROUNDS_COUNT):
        question, right_answer = build_question()

        answer = ask(question, answer_type)
        correct = check_answer(answer, right_answer, user_name)

        if not correct:
            return

    congratulate_user(user_name)


def welcome_user() -> str:
    """
    Ask and return user name.

    Returns:
        str
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
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
    print('Congratulations, {0}!'.format(user_name))


def generate_random_int(only_positive: bool = False) -> int:
    """Return random integer.

    Args:
        only_positive: if True return only positive number

    Returns:
        int
    """
    return randint(1 if only_positive else RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)


def ask(question: str, answer_type: Any) -> str:
    """
    Ask question and return user's answer.

    Wrapper function. Execute specific function for ask user.

    Args:
        question: question for user
        answer_type: available type of users's answer

    Returns:
        str

    """
    handlers = {bool: ask_yes_no, int: ask_int}
    ask_user = handlers[answer_type]

    return ask_user(question)


def ask_yes_no(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers: 'yes' and 'no', otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')
    while answer not in {'yes', 'no'}:
        answer = prompt.string('Answer "yes" or "no". Your answer: ')
    return answer


def ask_int(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers is correct integer, otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print('Question: {0}'.format(question))
    return str(prompt.integer('Your answer: ', empty=False))
