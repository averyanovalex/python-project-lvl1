"""Calc game."""

from random import choice

from brain_games.common import ask_int, generate_random_int, run_game


def brain_calc() -> None:
    """Implementaion of game's logic."""
    run_game(
        welcome_message='What is the result of the expression?',
        build_question=build_question_and_answer,
        ask_question=ask_int,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate 2 numbers , math operation, calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number1 = generate_random_int()
    number2 = generate_random_int()
    mark, function = generate_random_math_operation()

    right_answer = str(function(number1, number2))

    return compile_question(number1, mark, number2), right_answer


def generate_random_math_operation() -> tuple:
    """
    Generate random math operation.

    Returns:
        str, def
    """
    math_operations = [('+', add), ('-', diff), ('*', multiply)]
    return choice(math_operations)


def add(number1: int, number2: int) -> int:
    """
    Calculate sum.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    return number1 + number2


def diff(number1: int, number2: int) -> int:
    """
    Calculate difference.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    return number1 - number2


def multiply(number1: int, number2: int) -> int:
    """
    Calculate multiplication.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    return number1 * number2


def compile_question(substring1, substring2, substring3) -> str:
    """
    Compile question for user as string.

    Args:
        substring1: first substring
        substring2: second substring
        substring3: third substring

    Returns:
        str
    """
    return '{0} {1} {2}'.format(substring1, substring2, substring3)
