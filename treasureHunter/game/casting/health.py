import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Health(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by crashing the other player.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._health = 100
        self.add_health(100)
        self._position = (Point(0,15))

    def add_health(self, health):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self.set_text(f"Health: {self._health}")