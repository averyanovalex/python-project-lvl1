"""Greatest Common Devizor game."""

from brain_games.cli import answer_int, print_text, welcome_user
from brain_games.games.common import (
    ROUNDS,
    calc_gcd,
    check_answer,
    congratulate_user,
    random_int,
)


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

    question = 'Question: {s1} {s2}'.format(s1=str(num1), s2=str(num2))
    right_answer = str(calc_gcd(num1, num2))

    return question, right_answer


def brain_gcd() -> None:
    """Implementaion of game's logic."""
    name = welcome_user()
    print_text('Find the greatest common divisor of given numbers.')

    for _ in range(ROUNDS):
        question, right_answer = prepare_question_and_answer()

        answer = answer_int(question)
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)
