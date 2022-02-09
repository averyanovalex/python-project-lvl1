"""Calc game."""

from random import choice

from brain_games.cli import answer_int, print_text, welcome_user
from brain_games.games.common import (
    ROUNDS,
    check_answer,
    congratulate_user,
    random_int,
)


def add(num1: int, num2: int) -> int:
    """
    Calculate sum.

    Args:
        num1: first number
        num2: second number

    Returns:
        int
    """
    return num1 + num2


def diff(num1: int, num2: int) -> int:
    """
    Calculate difference.

    Args:
        num1: first number
        num2: second number

    Returns:
        int
    """
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    """
    Calculate multiplication.

    Args:
        num1: first number
        num2: second number

    Returns:
        int
    """
    return num1 * num2


def random_math_operation() -> tuple:
    """
    Generate random math operation.

    Returns:
        str, def
    """
    math_ops = [('+', add), ('-', diff), ('*', multiply)]
    return choice(math_ops)


def question_as_str(substr1, substr2, substr3) -> str:
    """
    Compile question for user as string.

    Args:
        substr1: first substring
        substr2: second substring
        substr3: third substring

    Returns:
        str
    """
    return 'Question: {s1} {s2} {s3}'.format(s1=substr1, s2=substr2, s3=substr3)


def prepare_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate 2 numbers , math operation, calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    num1 = random_int()
    num2 = random_int()
    mark, func = random_math_operation()

    right_answer = str(func(num1, num2))

    return question_as_str(num1, mark, num2), right_answer


def brain_calc() -> None:
    """Implementaion of game's logic."""
    name = welcome_user()
    print_text('What is the result of the expression?')

    for _ in range(ROUNDS):
        question, right_answer = prepare_question_and_answer()

        answer = str(answer_int(question))
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)
