"""Calc game."""

from random import choice

from brain_games.common import answer_int, random_int, run_game


def brain_calc() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'What is the result of the expression?'
    build_question = prepare_question_and_answer
    ask_question = answer_int

    run_game(welcome_message, build_question, ask_question)


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


def random_math_operation() -> tuple:
    """
    Generate random math operation.

    Returns:
        str, def
    """
    math_ops = [('+', add), ('-', diff), ('*', multiply)]
    return choice(math_ops)


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
    return '{0} {1} {2}'.format(substr1, substr2, substr3)
