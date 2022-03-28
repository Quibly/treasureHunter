from game.casting.actor import Actor
from game.shared.point import Point
import random
import constants

class Trap(Actor):
    """
    An item meant to disrupt the archeoligists from increasing their riches. 
    
    The responsibility of an Trap is to take away player energy.

    Attributes:
        _damage(int): The amount of damage a player takes if they contact this trap.
    """
    def __init__(self):
        """
        Holds the damage amount from the trap
        """
        super().__init__()
        self._damage = 50
        self._prepare_trap()

    def get_damage(self):
        """Returns the damage amount of the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        return self._damage

    def set_damage(self, damage):
        """Updates the damage amount from contacting the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        self._damage = damage

    def _prepare_trap(self):
        """
        """
        text = "O"

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        self.set_text(text)
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.BLACK)
        self.set_position(position)
        self.set_damage(constants.TRAP_DAMAGE)
