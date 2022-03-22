from game.casting.actor import Actor

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
        self._damage = -50

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
