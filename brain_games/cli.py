"""Command line interface for brain-games."""

import prompt


def print_text(text: str) -> None:
    """
    Print text into command line interface.

    Args:
        text: text for print
    """
    print(text)


def welcome_user() -> str:
    """
    Ask and return user name.

    Returns:
        str
    """
    print_text('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print_text('Hello, {name}!'.format(name=name))
    return name


def answer_yes_no(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers: 'yes' and 'no', otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print_text(question)
    answer = prompt.string('Your answer: ')
    while answer not in {'yes', 'no'}:
        answer = prompt.string('Answer "yes" or "no". Your answer: ')
    return answer


def answer_int(question: str) -> str:
    """
    Ask question and return user's answer.

    Correct answers is correct integer, otherwise ask user again.

    Args:
        question: question for user

    Returns:
        str
    """
    print_text(question)
    return str(prompt.integer('Your answer: ', empty=False))
