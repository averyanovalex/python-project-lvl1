"""Progression game."""

from random import randint

from brain_games.common import ask_int, run_game

PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10
PROGRESSION_START_ITEM_MAX = 9
PROGRESSION_ITERATOR_MAX = 5


def brain_progression() -> None:
    """Implementaion of game's logic."""
    run_game(
        welcome_message='What number is missing in the progression?',
        build_question=build_question_and_answer,
        ask_question=ask_int,
    )


def build_question_and_answer() -> tuple:
    """
    Prepare question and correct answer as strings.

    Generate progression, choice missed item and generate question and answer.

    Returns:
        str, str
    """
    progression = generate_arithmetic_progression(
        len_min=PROGRESSION_LEN_MIN,
        len_max=PROGRESSION_LEN_MAX,
        start_item_max=PROGRESSION_START_ITEM_MAX,
        iterator_max=PROGRESSION_ITERATOR_MAX,
    )

    missed_item_index = choice_missed_item(progression)

    question = compile_question(progression, missed_item_index)
    right_answer = str(progression[missed_item_index])

    return question, right_answer


def generate_arithmetic_progression(
    len_min: int,
    len_max: int,
    start_item_max: int,
    iterator_max: int,
) -> list:
    """
    Generate arithmetic progression.

    Args:
        len_min: min len of pregression will be generated
        len_max: max len of pregression will be generated
        start_item_max: max value of start item
        iterator_max: max value of iterator

    Returns:
        list[int]
    """
    progression_len = randint(len_min, len_max)
    start_item = randint(1, start_item_max)
    iterator = randint(1, iterator_max)

    last_element = start_item + iterator * progression_len
    return list(range(start_item, last_element + 1, iterator))


def choice_missed_item(progression: list) -> int:
    """
    Choice missed item in progression and return index.

    Args:
        progression: generated arithmetic progression

    Returns:
        int
    """
    return randint(0, len(progression) - 1)


def compile_question(progression: list, missed_item_index: int) -> str:
    """
    Build question as string from progression (list) and missed item.

    Args:
        progression: generated arithmetic progression
        missed_item_index: index of missed element

    Returns:
        str
    """
    progression_as_str = ''
    for index, progression_item in enumerate(progression):
        item_as_str = '..' if index == missed_item_index else str(progression_item)
        progression_as_str += '{0} '.format(item_as_str)

    return progression_as_str[:-1]
