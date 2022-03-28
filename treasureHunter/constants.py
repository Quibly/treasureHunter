from game.shared.color import Color
import os

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
POWDER_BLUE = Color(240 ,248, 255)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
TAN = Color(160, 82, 45)
TREASURE_VALUE = 1
TRAP_DAMAGE = 50
DEFAULT_TREASURES = 6
DEFAULT_TRAPS = 4
HUNTERS = 2
HUNTER_HEALTH = 100
