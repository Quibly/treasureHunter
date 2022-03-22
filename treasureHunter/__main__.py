import os
import random

from game.casting.actor import Actor
from game.casting.ground_cover import Ground_Cover
from game.casting.treasure import Treasure
from game.casting.trap import Trap
from game.casting.hunter import Hunter
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
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
HUNTERS = 1


def main():
    """
    Controls the main initialization of the game and starts it
    """

    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the hunters
    x = int(MAX_X / 4)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    for i in range(HUNTERS):
        if i == 2:
            position = Point(x*3,y)
        hunter = Hunter()
        hunter.set_text("#")
        hunter.set_font_size(FONT_SIZE)
        hunter.set_color(POWDER_BLUE)
        hunter.set_position(position)
        cast.add_actor("hunters", hunter)

    
    # create the ground cover
    for i in range(COLS):
        for j in range(ROWS):
            text = chr(random.randint(33, 126))
            position = Point(i,j)
            position = position.scale(CELL_SIZE)
            
            ground_cover = Ground_Cover()
            ground_cover.set_text(text)
            ground_cover.set_font_size(FONT_SIZE)
            ground_cover.set_color(TAN)
            ground_cover.set_position(position)
            cast.add_actor("ground_covers", ground_cover)

    # create the treasures
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_TREASURES):
        text = "X"
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        
        treasure = Treasure()
        treasure.set_text(text)
        treasure.set_font_size(FONT_SIZE)
        treasure.set_color(BLACK)
        treasure.set_position(position)
        treasure.set_message(message)
        treasure.set_value(TREASURE_VALUE)
        cast.add_actor("treasures", treasure)

    # create the traps
    for n in range(DEFAULT_TRAPS):
        text = "O"

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        trap = Trap()
        trap.set_text(text)
        trap.set_font_size(FONT_SIZE)
        trap.set_color(BLACK)
        trap.set_position(position)
        trap.set_damage(TRAP_DAMAGE)
        cast.add_actor("traps", trap)
                
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
