"""
Runs the game.
Please run this file with the following command:
python -m run_game
"""

import sys

from escape_velocity.__main__ import main

# The major, minor version numbers your require
MIN_VER = (3, 10)

if sys.version_info[:2] < MIN_VER:
    sys.exit("This game requires Python {}.{}.".format(*MIN_VER))

if __name__ == "__main__":
    main()
