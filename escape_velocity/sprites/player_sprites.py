"""
The player sprite class.
"""

import math

import arcade
from arcade import key as k

from ..constants import PLAYER_DIR, PLAYER_SPEED, PLAYER_ROTATION


class Player(arcade.Sprite):
    def __init__(self, game):
        super().__init__(PLAYER_DIR / "rover.png")

        self.game = game

        self.speed = PLAYER_SPEED
        self.rotation = PLAYER_ROTATION

        self.setup()

    def setup(self):
        self.game.scene.add_sprite("player", self)

        # Place player on landing pad
        self.center_x, self.center_y = 150, 350

        self.game.physics_engine.add_collision_handler(
            "player", "ground", post_handler=self.hit_ground
        )

        self.apply_physics()

    def update(self, delta_time: float = 1 / 60):
        """Update the player"""

        player_physics_object = self.game.physics_engine.get_physics_object(self)

        # Rotate the player physics object
        if k.LEFT in self.game.pressed_keys:
            player_physics_object.body.angle += self.rotation
        if k.RIGHT in self.game.pressed_keys:
            player_physics_object.body.angle -= self.rotation

        # Apply force upwards on the player
        if k.UP in self.game.pressed_keys:
            self.game.physics_engine.apply_force(
                self,
                (0, PLAYER_SPEED * math.cos(math.radians(self.angle))),
            )

    def apply_physics(self):
        self.game.physics_engine.add_sprite_list(
            self.game.scene["player"],
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            collision_type="player",
            mass=0.11,
            damping=0.5,
        )

    def hit_ground(self, *args):
        self.game.setup()
