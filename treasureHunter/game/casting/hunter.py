from game.casting.actor import Actor
from game.shared.point import Point
import constants
from constants import HUNTER_HEALTH

class Hunter(Actor):
    """
    An object to define the player Hunter attributes. 
    
    The responsibility of a Hunter is to house health, scoring, and controls for the player hunters.

    Attributes:
        _health(int): The amount of damage a player takes if they contact this trap.
    """
    def __init__(self, player_number):
        """
        Holds the damage amount from the trap
        """
        super().__init__()
        self._player_number = 1
        self._prepare_hunter(player_number)

    def get_player_number(self):
        """
        """
        return self._player_number
    
    def set_player_number(self, player_number):
        """
        """
        self._player_number = player_number

    def _prepare_hunter(self, player_number):
        """
        """
        if player_number == 1:
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y - constants.CELL_SIZE)
            position = Point(x, y)
            self.set_color(constants.BLUE)
        elif player_number == 2:
            x = int((constants.MAX_X * 3) / 4)
            y = int(constants.MAX_Y - constants.CELL_SIZE)
            position = Point(x, y)
            self.set_color(constants.ORANGE)
        text = "#"
        self.set_text(text)
        self.set_font_size(constants.FONT_SIZE)
        self.set_position(position)
        self.set_player_number(player_number)
