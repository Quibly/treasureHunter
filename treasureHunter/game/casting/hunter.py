from game.casting.actor import Actor

class Hunter(Actor):
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
        self._health = 100

    def get_health(self):
        """Returns the damage amount of the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        return self._health
    
    def change_health(self, change):
        """Updates the damage amount from contacting the trap.
        
        Args:
            _damage(int): The amount of damage a player takes if they contact this trap.
        """
        health = self._health
        self._health = int(change) + health
