#!/usr/bin/env python
"""Game 'Even'  entrypoint."""

from brain_games.game_engine import run_game
from brain_games.games import brain_even as game


def main() -> None:
    """Run game."""
    run_game(game)


if __name__ == '__main__':
    main()
