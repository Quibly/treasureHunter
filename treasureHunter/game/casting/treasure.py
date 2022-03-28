from game.casting.actor import Actor
import constants
from game.shared.point import Point
from game.casting.cast import Cast
import random


class Treasure(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of a Treasure is to provide a message about itself and hold the value until its found.

    Attributes:
        _message (string): A short description about the treasure.
        _value(integer): The given value.
    """
    def __init__(self):
        """
        _message(string): details for gameplay.
        _value(integer): The given value.
        """
        super().__init__()
        self._message = ""
        self._value = int(1)
        self._prepare_treasure()
                
    def get_message(self):
        """Gets the treasure's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_value(self):
        """Gets the treasure value.
        
        Returns:
            integer: The value of the treasure.
        """
        value = self._value
        return value

    def set_value(self, value):
        """Updates the value to the given one.
        
        Args:
            _value(integer): The given value.
        """
        self._value = int(value)

    def _prepare_treasure(self):
        """
        """
        with open(constants.DATA_PATH) as file:
            data = file.read()
            messages = data.splitlines()

        cast = Cast()   
        treasures = cast.get_actors("treasures")

        text = "X"
        message = messages[len(treasures)]

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        
        self.set_text(text)
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.BLACK)
        self.set_position(position)
        self.set_message(message)
        self.set_value(constants.TREASURE_VALUE)
