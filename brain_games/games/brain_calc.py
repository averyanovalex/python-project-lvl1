"""Calc game."""

from operator import add, mul, sub
from random import choice

from brain_games.common import generate_random_int

main_question = 'What is the result of the expression?'


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

    return f'{number1} {mark} {number2}', right_answer


def generate_random_math_operation() -> tuple:
    """
    Generate random math operation.

    Returns:
        str, def
    """
    math_operations = [('+', add), ('-', sub), ('*', mul)]
    return choice(math_operations)
