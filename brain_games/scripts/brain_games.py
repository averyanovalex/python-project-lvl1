#!/usr/bin/env python
"""Brain_games entrypoint."""

from brain_games.cli import welcome_user


def main() -> None:
    """Entrypoint function."""
    welcome_user()


if __name__ == '__main__':
    main()
