"""Even game."""

from brain_games.common import generate_random_int, run_game


def brain_even() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(
        welcome_message=welcome_message,
        build_question=build_question_and_answer,
        answer_type=bool,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate number.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number = generate_random_int()
    question = str(number)
    right_answer = 'yes' if number % 2 == 0 else 'no'

    return question, right_answer
