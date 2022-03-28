from game.scripting.action import Action



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
        velocity1 = self._keyboard_service.get_direction1()
        velocity2 = self._keyboard_service.get_direction2()
        for hunter in hunters:
            if hunter.get_player_number() == 1:
                hunter.set_velocity(velocity1)
            elif hunter.get_player_number() == 2:
                hunter.set_velocity(velocity2)
