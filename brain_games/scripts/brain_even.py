#!/usr/bin/env python
"""Game 'Even'  entrypoint."""

from brain_games.games.brain_even import brain_even
from brain_games.cli import welcome_user

def main():
    """Entrypoint function."""
    welcome_user()
    brain_even()


if __name__ == '__main__':
    main()
