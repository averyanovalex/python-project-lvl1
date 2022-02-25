"""Prime number game."""

from brain_games.common import generate_random_int, run_game


def brain_prime() -> None:
    """Implementaion of game's logic."""
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(
        main_question=question,
        answer_type=bool,
        build_question=build_question_and_answer,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate number , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number = generate_random_int(only_positive=True)

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
    if number == 0:
        return False

    for devisor in range(2, abs(number) // 2 + 1):
        if number % devisor == 0:
            return False

    return True
