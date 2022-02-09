"""Prime number game."""

from brain_games.cli import answer_yes_no, print_text, welcome_user
from brain_games.games.common import (
    ROUNDS,
    calc_gcd,
    check_answer,
    congratulate_user,
    random_int,
)


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


def brain_prime() -> None:
    """Implementaion of game's logic."""
    name = welcome_user()
    print_text('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(ROUNDS):
        question, right_answer = prepare_question_and_answer()

        answer = answer_yes_no(question)
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)
