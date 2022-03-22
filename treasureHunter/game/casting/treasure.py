from game.casting.actor import Actor


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
        

        
