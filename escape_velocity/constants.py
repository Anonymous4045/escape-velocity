"""
Constant values used by all modules.
"""

from pathlib import Path


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

# Player information
PLAYER_SPEED = 100
PLAYER_ROTATION = 0.05
