"""Even game."""

from brain_games.cli import answer_yes_no, print_text, welcome_user
from brain_games.games.common import (
    ROUNDS,
    check_answer,
    congratulate_user,
    random_int,
)


def brain_even() -> None:
    """Implementaion of game's logic."""
    name = welcome_user()
    print_text('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS):
        number = random_int()
        right_answer = 'yes' if number % 2 == 0 else 'no'

        answer = answer_yes_no('Question: {number}'.format(number=number))
        is_correct = check_answer(answer, right_answer, name)

        if not is_correct:
            return

    congratulate_user(name)
