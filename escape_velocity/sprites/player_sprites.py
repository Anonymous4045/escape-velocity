"""
The player sprite class.
"""

from ..constants import *


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(PLAYER_DIR / "rover.png")
