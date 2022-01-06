#!/usr/bin/env python
"""Module contain entry points."""

from brain_games.cli import welcome_user


def main():
    """Entrypoint function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
