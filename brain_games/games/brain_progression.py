"""Progression game."""

from random import randint

from brain_games.cli import answer_int
from brain_games.games.common import run_game

PROGRESSION_LEN_MIN = 5
PROGRESSION_LEN_MAX = 10
PROGRESSION_START_ELEMENT_MAX = 9
PROGRESSION_ITERATOR_MAX = 5


def brain_progression() -> None:
    """Implementaion of game's logic."""
    run_game(
        welcome_message='What number is missing in the progression?',
        build_question=prepare_question_and_answer,
        ask_question=answer_int,
    )


def prepare_question_and_answer() -> tuple:
    """
    Prepare question and correct answer as strings.

    Generate progression, choice missed item and generate question and answer.

    Returns:
        str, str
    """
    progression = generate_progression()
    missed_item = choice_missed_item(progression)

    question = question_as_str(progression, missed_item)
    right_answer = str(progression[missed_item])

    return question, right_answer


def generate_progression() -> list:
    """
    Generate arithmetic progression.

    Returns:
        list[int]
    """
    progr_len = randint(PROGRESSION_LEN_MIN, PROGRESSION_LEN_MAX)
    start_item = randint(1, PROGRESSION_START_ELEMENT_MAX)
    iterator = randint(1, PROGRESSION_ITERATOR_MAX)

    last_element = start_item + iterator * progr_len
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


def question_as_str(progression: list, missed_item: int) -> str:
    """
    Build question as string from progression (list) and missed item.

    Args:
        progression: generated arithmetic progression
        missed_item: index of missed element

    Returns:
        str
    """
    progression_str = ''
    for index, progr_item in enumerate(progression):
        item_str = '..' if index == missed_item else str(progr_item)
        progression_str += '{0} '.format(item_str)

    return 'Question: {0}'.format(progression_str[:-1])
