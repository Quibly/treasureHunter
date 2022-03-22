from game.casting.actor import Actor

class Ground_Cover(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _display_toggle(int): Controls the display of ground cover:
        A display toggle of 0 = no display.
        A display toggle of 1 = display. (Default)
    """
    def __init__(self):
        """
        Sets a default display toggle variable for ground cover.
    
        """
        super().__init__()
        self._display_toggle = 1
                
    def get_display_toggle(self):
        """Gets the ground covers display toggle.
        
        Returns:
            _display_toggle(int): Controls the display of ground cover:
        """
        return self._display_toggle
    
    def set_display_toggle(self, display_toggle):
        """
        Sets the ground cover display toggle

        Arguments:
            _display_toggle(int): Controls the display of ground cover
        """
        self._display_toggle = display_toggle
