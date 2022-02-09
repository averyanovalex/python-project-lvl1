"""Prime number game."""

from brain_games.cli import answer_yes_no
from brain_games.games.common import calc_gcd, random_int, run_game


def brain_prime() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    build_question = prepare_question_and_answer
    ask_question = answer_yes_no

    run_game(welcome_message, build_question, ask_question)


def prepare_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate number , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    num = random_int()

    question = 'Question: {s1}'.format(s1=str(num))
    right_answer = 'yes' if is_prime(num) else 'no'

    return question, right_answer


def is_prime(number: int) -> bool:
    """
    Calculate number is prime or not.

    Args:
        number: number fo calculate

    Returns:
        bool
    """
    if number in {1, 2}:
        return True

    for candidate in range(2, number - 1):
        gcd = calc_gcd(number, candidate)
        if gcd > 1:
            return False

    return True
