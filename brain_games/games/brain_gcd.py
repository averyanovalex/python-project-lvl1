"""Greatest Common Devizor game."""

from brain_games.common import generate_random_int

main_question = 'Find the greatest common divisor of given numbers.'


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer for user.

    Generate 2 numbers , calculate answer.
    Prepare question and correct answer as strings.

    Returns:
        str, str
    """
    number1 = generate_random_int(only_positive=True)
    number2 = generate_random_int(only_positive=True)

    question = f'{number1} {number2}'
    right_answer = str(calculate_gcd(number1, number2))

    return question, right_answer


def calculate_gcd(number1: int, number2: int) -> int:
    """
    Calulate greatest common devizor.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    min_number = min(number1, number2)
    max_candidate = min_number + 1
    gcd = 1
    for candidate in range(2, max_candidate):
        if number1 % candidate == 0 and number2 % candidate == 0:
            gcd = candidate

    return gcd
