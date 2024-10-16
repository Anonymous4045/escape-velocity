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

        self.game: arcade.Window = game

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
        if self.check_pressed(k.LEFT, k.A):
            player_physics_object.body.angle += self.rotation
        if self.check_pressed(k.RIGHT, k.D):
            player_physics_object.body.angle -= self.rotation

        # Apply force upwards on the player
        if self.check_pressed(k.UP, k.W, k.SPACE):
            self.game.physics_engine.apply_force(
                self,
                (0, PLAYER_SPEED * math.cos(math.radians(self.angle))),
            )

    def check_pressed(self, *keys: list[int]):
        """Checks if any of the given keys are pressed"""

        return any(key in self.game.pressed_keys for key in keys)

    def apply_physics(self):
        self.game.physics_engine.add_sprite_list(
            self.game.scene["player"],
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            collision_type="player",
            mass=0.11,
            damping=0.5,
        )

    def hit_ground(self, *args):
        """Player collided with the ground"""

        self.game.setup()
