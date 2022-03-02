"""Engine for all games."""

import prompt

ROUNDS_COUNT = 3


def run_game(game) -> None:
    """
    Implement common logic for all games.

    Args:
        game: module with specific game's logic
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.MAIN_QUESTION)

    for _ in range(ROUNDS_COUNT):
        question, right_answer = game.build_question_and_answer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ', empty=True)

        if answer == right_answer:
            print('Correct!')
        else:
            template = "'{s1}' is wrong answer ;(. Correct answer was '{s2}'."
            print(template.format(s1=answer, s2=right_answer))
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
