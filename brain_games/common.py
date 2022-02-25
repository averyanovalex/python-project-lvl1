"""Common functions and settings for all games."""

from random import randint
from typing import Any, Callable

import prompt
from brain_games.cli import welcome_user

RANDOM_NUMBER_MIN = -10
RANDOM_NUMBER_MAX = 50
ROUNDS_COUNT = 3


def run_game(
    main_question: str,
    answer_type: Any,
    build_question: Callable,
) -> None:
    """
    Engine for all games.

    This function implements common logic for any game.

    Args:
        main_question: question is displayed at the beginning of the game
        answer_type: available type of users's answer in game
        build_question: function to build question and right answer
    """
    user_name = welcome_user()

    print(main_question)

    for _ in range(ROUNDS_COUNT):
        question, right_answer = build_question()

        answer = ask(question, answer_type)
        correct = check_answer(answer, right_answer, user_name)

        if not correct:
            return

    print('Congratulations, {0}!'.format(user_name))


def ask(question: str, answer_type: Any = str) -> str:
    """
    Ask question and return user's answer.

    Args:
        question: question for user
        answer_type: available type of users's answer

    Returns:
        str

    """
    print('Question: {0}'.format(question))
    return prompt.string('Your answer: ')


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


def generate_random_int(only_positive: bool = False) -> int:
    """Return random integer.

    Args:
        only_positive: if True return only positive number

    Returns:
        int
    """
    return randint(1 if only_positive else RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
