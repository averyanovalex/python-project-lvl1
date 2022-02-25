"""Calc game."""

from operator import add, mul, sub
from random import choice

from brain_games.common import generate_random_int


def get_welcome_game_question() -> str:
    """
    Get welcome main game question to ask user at start.

    Returns:
        str
    """
    return 'What is the result of the expression?'


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
    math_operations = [('+', add), ('-', sub), ('*', mul)]
    return choice(math_operations)


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
