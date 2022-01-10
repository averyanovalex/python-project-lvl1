
"""Even game."""

from random import randint

from brain_games.cli import answer_yes_no, print_text, welcome_user

MIN_NUMBER = 1
MAX_NUMBER = 100
TRY_COUNT = 3


def brain_even():
    """Implementaion of game's logic."""
    name = welcome_user()
    print_text('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(TRY_COUNT):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        right_answer = 'yes' if number % 2 == 0 else 'no'

        print_text('Question: {number}'.format(number=number))
        answer = answer_yes_no()

        if answer == right_answer:
            print_text('Correct!')
        else:
            template = '"{s1}" is wrong answer ;(. Correct answer was "{s2}".'
            print_text(template.format(s1=answer, s2=right_answer))
            print_text("Let's try again, {s1}".format(s1=name))
            return

    print_text('Congratilations, {name}!'.format(name=name))
