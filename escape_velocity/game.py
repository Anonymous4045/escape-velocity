"""
This is the main game file. It contains the game class and all the game logic.
"""

from .constants import *
from .sprites.player_sprites import Player
from .sprites.level_sprites import Ground, LandingPad

from arcade import key as k


class MyGame(arcade.Window):
    """Class for all the game logic"""

    def __init__(self):
        print("Starting game...")

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.MAROON)

        self.scene: arcade.Scene = None

        self.physics_engine: arcade.PymunkPhysicsEngine = None

        self.player: Player = None

        self.setup()

    def setup(self):
        """Restart the game"""

        self.scene = arcade.Scene()

        self.physics_engine = arcade.PymunkPhysicsEngine(
            gravity=(0, -1000)
        )

        self.player = Player()
        self.player.center_x = 200
        self.player.center_y = 400
        self.scene.add_sprite("player", self.player)

        ground = Ground()
        self.scene.add_sprite("ground", ground)
        self.physics_engine.add_sprite(
            ground, body_type=arcade.PymunkPhysicsEngine.STATIC, collision_type="ground", friction=0.5, mass=1, moment=1
        )

        # Add landing pads
        for position in ((150, 200), (1200, 200)):
            landing_pad = LandingPad()
            landing_pad.center_x, landing_pad.center_y = position
            self.scene.add_sprite("landing_pad", landing_pad)

        self.physics_engine.add_sprite_list(
            self.scene["landing_pad"],
            body_type=arcade.PymunkPhysicsEngine.STATIC,
            collision_type="landing_pad",
        )

        # Place player on landing pad
        self.player.center_x, self.player.center_y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

        # Enable physics for the player
        self.physics_engine.add_sprite_list(
            self.scene["player"], body_type=arcade.PymunkPhysicsEngine.DYNAMIC, collision_type="player"
        )

        # Set up collision handlers
        self.physics_engine.add_collision_handler(
            'player', 'ground', post_handler=self.player_ground_collision
        )

    def on_draw(self):
        """Render the scene"""
        self.clear()

        # self.scene.draw()

        # Show hit boxes
        self.scene.draw_hit_boxes()

    def on_update(self, delta_time):
        """Update the scene"""

        self.scene.update()

        self.physics_engine.step(
            delta_time, True
            )

    def on_key_press(self, key_code, modifiers):
        '''Update set of pressed keys'''

        pressed.add(key_code)

    def on_key_release(self, key_code, modifiers):
        '''Update set of pressed keys'''

        pressed.remove(key_code)

    def player_ground_collision(self, *args, **kwargs):
        """Handle the player colliding with the ground"""

        logger.debug("Player collided with ground")

