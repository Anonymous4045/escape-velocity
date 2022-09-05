"""
Constant values used by all modules.
"""

import math
from pathlib import Path

from loguru import logger

import arcade

# Screen information
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Escape Velocity"

# File paths
REPO_ROOT = Path(__file__).parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
TILED_DIR = ASSETS_DIR / "tiled"
PLAYER_DIR = ASSETS_DIR / "player"
LEVELS_DIR = ASSETS_DIR / "levels"

# Key presses
pressed = set()

# Player information
PLAYER_SPEED = 100
PLAYER_ROTATION = 0.05
