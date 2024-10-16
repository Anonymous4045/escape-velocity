"""
This is the main game file. It contains the game class and all the game logic.
"""

import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from .sprites.level_sprites import Level
from .sprites.player_sprites import Player


class MyGame(arcade.Window):
    """Class for all the game logic"""

    def __init__(self):
        print("Starting game...")

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.MAROON)

        self.scene: arcade.Scene | None = None
        self.physics_engine: arcade.PymunkPhysicsEngine | None = None
        self.player: Player | None = None

        self.pressed_keys = None

        self.setup()

    def setup(self):
        """Restart the game"""

        self.physics_engine = arcade.PymunkPhysicsEngine(gravity=(0, -500))
        self.scene = Level(self)
        self.player = Player(self)

        self.pressed_keys = set()

    def on_draw(self):
        """Render the scene"""

        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
        """Update the scene"""

        self.scene.update()
        self.physics_engine.step(delta_time, True)

    def on_key_press(self, key_code, modifiers):
        """Update set of pressed keys"""

        if key_code not in self.pressed_keys:
            self.pressed_keys.add(key_code)

        if key_code == arcade.key.Q:
            self.close()

    def on_key_release(self, key_code, modifiers):
        """Update set of pressed keys"""

        if key_code in self.pressed_keys:
            self.pressed_keys.remove(key_code)
