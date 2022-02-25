#!/usr/bin/env python
"""Game 'Prime'  entrypoint."""

from brain_games.game_engine import run_game
from brain_games.games import brain_prime as game


def main() -> None:
    """Run game."""
    run_game(
        main_question=game.get_welcome_game_question(),
        build_question=game.build_question_and_answer,
    )


if __name__ == '__main__':
    main()
