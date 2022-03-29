from game.casting.actor import Actor
from game.shared.point import Point
import constants
from constants import HUNTER_HEALTH

class Hunter(Actor):
    """
    An object to define the player Hunter attributes. 
    
    The responsibility of a Hunter is to house health, scoring, and controls for the player hunters.

    Attributes:
        _player_number(int): Holds the player number value.
        _prepare_hunter(player_number) (function): A function that takes the player_number as input
            and creates the initial attributes of the hunter object. 
    """
    def __init__(self, player_number):
        """
        Creates the hunter objects and holds the player_number value.
        """
        super().__init__()
        self._player_number = 1
        self._prepare_hunter(player_number)

    def get_player_number(self):
        """
        Gets the player number value for the hunter object.

        Returns: 
            The player number.
        """
        return self._player_number
    
    def set_player_number(self, player_number):
        """
        Sets the player number for the hunter object.
        """
        self._player_number = player_number

    def _prepare_hunter(self, player_number):
        """
        A function that constructs the initial values for the hunter object attributes.
        It receives the player number and creates the hunter accordingly.
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
