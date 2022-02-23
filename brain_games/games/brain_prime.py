"""Prime number game."""

from brain_games.common import (
    ask_yes_no,
    calculate_gcd,
    generate_random_int,
    run_game,
)


def brain_prime() -> None:
    """Implementaion of game's logic."""
    welcome_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(
        welcome_message=welcome_message,
        build_question=build_question_and_answer,
        ask_question=ask_yes_no,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate number , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number = generate_random_int()

    question = str(number)
    right_answer = 'yes' if is_prime(number) else 'no'

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
        gcd = calculate_gcd(number, candidate)
        if gcd > 1:
            return False

    return True
