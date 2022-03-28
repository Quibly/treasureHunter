from game.casting.actor import Actor
from game.shared.point import Point
import constants
from constants import HUNTER_HEALTH

class Hunter(Actor):
    """
    An item meant to disrupt the archeoligists from increasing their riches. 
    
    The responsibility of an Trap is to take away player energy.

    Attributes:
        _damage(int): The amount of damage a player takes if they contact this trap.
    """
    def __init__(self, player_number):
        """
        Holds the damage amount from the trap
        """
        super().__init__()
        self._health = 100
        self._points = 0
        self._player_number = 1
        self._prepare_hunter(player_number)

    def get_health(self):
        """Returns the damage amount of the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        return self._health

    def set_health(self, health):
        """
        """
        self._health = health
    
    def trap_damage(self):
        """Updates the damage amount from contacting the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        self._health = self._health - 50
        
    def get_points(self):
        """
        """
        return self._points

    def set_points(self, points=0):
        """
        """
        self._points = self._points + points

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
        elif player_number == 2:
            x = int((constants.MAX_X * 3) / 4)
            y = int(constants.MAX_Y - constants.CELL_SIZE)
            position = Point(x, y)
        text = "#"
        self.set_text(text)
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.POWDER_BLUE)
        self.set_position(position)
        self.set_health(HUNTER_HEALTH)
        self.set_points()
        self.set_player_number(player_number)
