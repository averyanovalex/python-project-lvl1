"""Common functions and setings for all games."""

from random import randint

RANDOM_NUMBER_MIN = -10
RANDOM_NUMBER_MAX = 50
ROUNDS_COUNT = 3


def generate_random_int(only_positive: bool = False) -> int:
    """Return random integer.

    Args:
        only_positive: if True return only positive number

    Returns:
        int
    """
    return randint(1 if only_positive else RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
