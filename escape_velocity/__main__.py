"""
Set up and run the game.

This file should be run implicityly by executing {REPO_ROOT}/run_game.py.
"""

from .game import MyGame

import arcade


def main():
    """Run the game"""

    MyGame()
    arcade.run()


main()
