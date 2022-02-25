"""Engine for all games."""

from typing import Callable

from brain_games.cli import ask, print_text, welcome_user
from brain_games.common import ROUNDS_COUNT


def run_game(main_question: str, build_question: Callable) -> None:
    """
    Engine for all games.

    This function implements common logic for any game.

    Args:
        main_question: question is displayed at the beginning of the game
        build_question: function to build question and right answer
    """
    user_name = welcome_user()

    print_text(main_question)

    for _ in range(ROUNDS_COUNT):
        try:
            question, right_answer = build_question()
        except:
            print('TESTTTTTT')

        answer = ask(question)
        correct = check_answer(answer, right_answer, user_name)

        if not correct:
            return

    print_text('Congratulations, {0}!'.format(user_name))


def check_answer(answer: str, right_answer: str, user_name: str) -> bool:
    """
    Check correct users's answer or not.

    After checking, print message for user and return result.
    If user's answer is correct return True, otherwise  False.

    Args:
        answer: user's answer
        right_answer: correct answer
        user_name: user's name

    Returns:
        bool
    """
    if answer == right_answer:
        print_text('Correct!')
        return True

    template = "'{s1}' is wrong answer ;(. Correct answer was '{s2}'."
    print_text(template.format(s1=answer, s2=right_answer))
    print_text("Let's try again, {s1}!".format(s1=user_name))
    return False
