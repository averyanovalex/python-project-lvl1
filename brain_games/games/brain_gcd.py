"""Greatest Common Devizor game."""

from brain_games.common import answer_int, calc_gcd, random_int, run_game


def brain_gcd() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'Find the greatest common divisor of given numbers.'
    build_question = prepare_question_and_answer
    ask_question = answer_int

    run_game(welcome_message, build_question, ask_question)


def prepare_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate 2 numbers , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    num1 = random_int()
    num2 = random_int()

    question = '{0} {1}'.format(str(num1), str(num2))
    right_answer = str(calc_gcd(num1, num2))

    return question, right_answer
