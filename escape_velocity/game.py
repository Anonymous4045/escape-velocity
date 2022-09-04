'''
This is the main game file. It contains the game class and all the game logic.
'''

from .constants import *
from .sprites.player_sprite import Player


class MyGame(arcade.Window):
    '''Class for all the game logic'''
    def __init__(self):
        print('Starting game...')

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)

        self.scene: arcade.Scene = None

        self.setup()

    def setup(self):
        '''Restart the game'''

        self.scene = arcade.Scene()

    def on_draw(self):
        '''Render the scene'''

        self.clear()

        self.scene.draw()

    def on_update(self, delta_time):
        '''Update the scene'''

        self.scene.update()

