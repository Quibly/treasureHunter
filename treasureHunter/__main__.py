import constants
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


def main():
    """
    Controls the main initialization of the game and starts it
    """

    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the hunters
    x = int(constants.MAX_X / 4)
    y = int(constants.MAX_Y - constants.CELL_SIZE)
    position = Point(x, y)

    for i in range(constants.HUNTERS):
        if i == 2:
            position = Point(x*3,y)
        hunter = Hunter()
        hunter.set_text("#")
        hunter.set_font_size(constants.FONT_SIZE)
        hunter.set_color(constants.POWDER_BLUE)
        hunter.set_position(position)
        cast.add_actor("hunters", hunter)

    
    # create the ground cover
    for i in range(constants.COLS):
        for j in range(constants.ROWS):
            text = chr(random.randint(33, 126))
            position = Point(i,j)
            position = position.scale(constants.CELL_SIZE)
            
            ground_cover = Ground_Cover()
            ground_cover.set_text(text)
            ground_cover.set_font_size(constants.FONT_SIZE)
            ground_cover.set_color(constants.TAN)
            ground_cover.set_position(position)
            cast.add_actor("ground_covers", ground_cover)

    # create the treasures
    with open(constants.DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(constants.DEFAULT_TREASURES):
        text = "X"
        message = messages[n]

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        
        treasure = Treasure()
        treasure.set_text(text)
        treasure.set_font_size(constants.FONT_SIZE)
        treasure.set_color(constants.BLACK)
        treasure.set_position(position)
        treasure.set_message(message)
        treasure.set_value(constants.TREASURE_VALUE)
        cast.add_actor("treasures", treasure)

    # create the traps
    for n in range(constants.DEFAULT_TRAPS):
        text = "O"

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        trap = Trap()
        trap.set_text(text)
        trap.set_font_size(constants.FONT_SIZE)
        trap.set_color(constants.BLACK)
        trap.set_position(position)
        trap.set_damage(constants.TRAP_DAMAGE)
        cast.add_actor("traps", trap)
                
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
