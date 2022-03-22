import constants
from game.scripting.action import Action
from game.shared.point import Point


class MoveHunterAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's direction.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """
    def __init__(self, video_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._video_service = video_service


    def execute(self, cast, script):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        
        hunters = cast.get_actors("hunters")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        for hunter in hunters:
            hunter.move_next(max_x,max_y)