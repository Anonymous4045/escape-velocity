"""
Constant values used by all modules.
"""

from pathlib import Path
from loguru import logger

import arcade

# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Escape Velocity"

# File paths
REPO_ROOT = Path(__file__).parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
TILED_DIR = ASSETS_DIR / "tiled"
LEVELS_DIR = TILED_DIR / "levels"
