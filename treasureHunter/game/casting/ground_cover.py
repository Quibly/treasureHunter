from game.casting.actor import Actor
import constants
import random

class Ground_Cover(Actor):
    """
    An object for covering the traps and treasures hiding in the game field.

    Creates objects that represent ground cover for the game.

    Attributes:
        _display_toggle(int): Controls the display of ground cover:
            A display toggle of 0 = no display.
            A display toggle of 1 = display. (Default)
        _prepare_ground_cover() (function): A function to define the initial creation of ground cover.
    """
    def __init__(self, position):
        """
        Sets a default display toggle variable for ground cover
        and creates the initial attributes of the ground cover objects.
    
        """
        super().__init__()
        self._display_toggle = 1
        self._prepare_ground_cover(position)
                
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

    def _prepare_ground_cover(self, position):
        """
        A function to create the initial settings for the ground cover objects.
        The function adds text, color, position, and font_size for objects.
        """
        text = chr(random.randint(33, 126))
        self.set_text(text)
        self.set_position(position)
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.TAN)
