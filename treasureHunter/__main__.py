import constants
from game.casting.actor import Actor
from game.casting.ground_cover import Ground_Cover
from game.casting.treasure import Treasure
from game.casting.trap import Trap
from game.casting.hunter import Hunter
from game.casting.health import Health
from game.casting.score import Score
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point
from game.scripting.script import Script
from game.scripting.control_hunter_action import ControlHunterAction
from game.scripting.move_hunter_action import MoveHunterAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction


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
    
    # create the hunter(s)
    for i in range(constants.HUNTERS):
        cast.add_actor("hunters", Hunter())

    # create the ground cover
    for i in range(constants.COLS):
        for j in range(constants.ROWS):
            position = Point(i,j+constants.BANNER_HEIGHT)
            position = position.scale(constants.CELL_SIZE)
            cast.add_actor("ground_covers", Ground_Cover(position))

    # create the treasures 
    for n in range(constants.DEFAULT_TREASURES):
        cast.add_actor("treasures", Treasure())

    # create the traps
    for n in range(constants.DEFAULT_TRAPS):
        cast.add_actor("traps", Trap())

    #create score UI
    cast.add_actor("score", Score())

    #create health Ui
    cast.add_actor("health", Health())
                
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)

    script = Script()
    script.add_action("input", ControlHunterAction(keyboard_service))
    script.add_action("update", MoveHunterAction(video_service))
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(keyboard_service, video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
