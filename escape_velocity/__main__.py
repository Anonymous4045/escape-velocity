"""
Set up and run the game.

This file should be run implicitly by executing {REPO_ROOT}/run_game.py.
"""

import arcade

from .game import MyGame


def main():
    """Run the game"""

    MyGame()
    arcade.run()
