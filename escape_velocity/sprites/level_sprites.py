"""
Used for creating the level
"""

from ..constants import *


class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__(
            filename=LEVELS_DIR / "Level1.png", hit_box_algorithm="Detailed", hit_box_detail=1.0
        )
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2


class LandingPad(arcade.Sprite):
    def __init__(self):
        super().__init__(
            filename=LEVELS_DIR / "landing_pad.png", hit_box_algorithm="Detailed"
        )
