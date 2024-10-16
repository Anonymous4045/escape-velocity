"""
Used for creating the level
"""

import arcade

from ..constants import LEVELS_DIR, SCREEN_HEIGHT, SCREEN_WIDTH


class Level(arcade.Scene):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.setup()

    def setup(self):
        self.add_ground()
        self.add_landing_pads()

    def add_landing_pads(self):
        """Add landing pads"""

        y = 235
        for position in ((150, y), (1200, y)):
            landing_pad = LandingPad()
            landing_pad.center_x, landing_pad.center_y = position
            self.add_sprite("landing_pad", landing_pad)
        self.game.physics_engine.add_sprite_list(
            self["landing_pad"],
            body_type=arcade.PymunkPhysicsEngine.STATIC,
            collision_type="landing_pad",
            friction=100,  # A lot of friction to make the player stick
        )

    def add_ground(self):
        """Add ground to the map"""

        ground = Ground()
        self.add_sprite("ground", ground)
        self.game.physics_engine.add_sprite(
            ground, body_type=arcade.PymunkPhysicsEngine.STATIC, collision_type="ground"
        )


class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__(
            filename=LEVELS_DIR / "flat_ground.png",
            hit_box_algorithm="Detailed",
            hit_box_detail=1.0,
        )
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.add_spatial_hashes()


class LandingPad(arcade.Sprite):
    def __init__(self):
        super().__init__(
            filename=LEVELS_DIR / "landing_pad.png", hit_box_algorithm="Detailed"
        )
