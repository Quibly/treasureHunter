import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlHunterAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's direction.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        hunters = cast.get_actors("hunters")
        velocity = self._keyboard_service.get_direction()
        for hunter in hunters:
            hunter.set_velocity(velocity)