"""Greatest Common Devizor game."""

from brain_games.common import (
    ask_int,
    calculate_gcd,
    generate_random_int,
    run_game,
)


def brain_gcd() -> None:
    """Implementaion of game's logic."""
    run_game(
        welcome_message='Find the greatest common divisor of given numbers.',
        build_question=build_question_and_answer,
        ask_question=ask_int,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate 2 numbers , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number1 = generate_random_int()
    number2 = generate_random_int()

    question = '{0} {1}'.format(str(number1), str(number2))
    right_answer = str(calculate_gcd(number1, number2))

    return question, right_answer
