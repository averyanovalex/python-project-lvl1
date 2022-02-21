"""Even game."""

from brain_games.common import answer_yes_no, random_int, run_game


def brain_even() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'Answer "yes" if the number is even, otherwise answer "no".'
    build_question = prepare_question_and_answer
    ask_question = answer_yes_no

    run_game(welcome_message, build_question, ask_question)


def prepare_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate number.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number = random_int()
    question = 'Question: {number}'.format(number=number)
    right_answer = 'yes' if number % 2 == 0 else 'no'

    return question, right_answer
