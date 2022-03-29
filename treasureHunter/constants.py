from game.shared.color import Color
import os

"""
Constant settings for the program funcionality.
"""

FRAME_RATE = 12
BANNER_HEIGHT = 4
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
MAX_X = 900
MAX_Y = 600 + (BANNER_HEIGHT * CELL_SIZE)
CAPTION = "Treasure Hunter"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
BLUE = Color(100, 100, 255)
ORANGE = Color(255, 165, 0)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
TAN = Color(160, 82, 45)
GREEN = Color(0, 128, 0)
YELLOW = Color(255, 255, 0)
TREASURE_VALUE = 1
TRAP_DAMAGE = 50
DEFAULT_TREASURES = 6
DEFAULT_TRAPS = 4
HUNTERS = 2
HUNTER_HEALTH = 100
