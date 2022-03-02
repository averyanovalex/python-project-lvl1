"""Engine for all games."""

import prompt

ROUNDS_COUNT = 3


def run_game(game) -> None:
    """
    Implement common logic for all games.

    Args:
        game: module with specific game's logic
    """
    user_name = welcome_user()

    print_text(game.get_welcome_game_question())

    for _ in range(ROUNDS_COUNT):
        question, right_answer = game.build_question_and_answer()

        answer = ask(question)
        if answer == right_answer:
            print_text('Correct!')
        else:
            template = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
            print_text(template.format(answer, right_answer))
            print_text("Let's try again, {0}!".format(user_name))
            return

    print_text('Congratulations, {0}!'.format(user_name))


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


def ask(question: str) -> str:
    """
    Ask question and return user's answer.

    Args:
        question: question for user

    Returns:
        str

    """
    print_text('Question: {0}'.format(question))
    return prompt.string('Your answer: ', empty=True)
