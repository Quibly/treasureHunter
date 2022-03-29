from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
import constants
from constants import HUNTER_HEALTH
from constants import TREASURE_VALUE
from constants import TRAP_DAMAGE

class Banner(Actor):
    """
        A class to hold methods for the banner display on the game.
        This keeps tracker of playing health and scoring also.

    Attributes:
        _score1 (int): Player 1s current score.
        _score2 (int): Player 2s current score.
        _health1 (int): Player 1s health number.
        _health2 (int): Player 2s health number.
        _message (string): The message to be displayed for collisions.
        _prepare_banner() (function): Method for initial creation of banner objects.
    """
    def __init__(self):
        """
        Constructs a new banner object.
        """
        super().__init__()
        self._score1 = 0
        self._score2 = 0
        self._health1 = HUNTER_HEALTH
        self._health2 = HUNTER_HEALTH
        self._message = ''
        self._prepare_banner()

    def set_message(self, message):
        """
        Sets the message text to be displayed in the banner when collisions happen.
        """
        self._message = message
    
    def set_treasure_gain1(self, points):
        """
        Sets the new score for Player 1 after treasure collision.
        """
        self._score1 = self._score1 + points

    def set_treasure_gain2(self, points):
        """
        Sets the new score for Player 2 after treasure collision.
        """
        self._score2 = self._score2 + points
    
    def set_trap_damage1(self, damage):
        """
        Sets the new health value for Player 1 after trap collision.
        """
        self._health1 = self._health1 - damage

    def set_trap_damage2(self, damage):
        """
        Sets the new health value for Player 2 after trap collision.
        """
        self._health2 = self._health2 - damage

    def get_health1(self):
        """
        Gets the health value for Player 1.

        Returns:
            Player 1 health value.
        """
        return self._health1

    def get_health2(self):
        """
        Gets the health value for Player 2.

        Returns:
            Player 2 health value.
        """
        return self._health2

    def display_banner(self):
        """
        Displays the current values for the Banner() object.
        This houses the main structure of the banner display.
        """
        self.set_text(f'Player 1 Score: {self._score1}                             Player 2 Score: {self._score2}\nPlayer 1 Health: {self._health1}                          Player 2 Health: {self._health2}\n{self._message}')

    def _prepare_banner(self):
        """
        Prepares the initial Banner() object structure.
        Creates text, font size, color, and position settings for the banner object.
        """
        cast = Cast()
        
        hunters = cast.get_actors("hunters")
        #Checks for player number and updates appropriate banner field.
        for hunter in hunters:
            if hunter.get_player_number() == 1:
                self._score1 = hunter.get_points()
                self._health1 = hunter.get_health()
            elif hunter.get_player_number() == 2:
                self._score2 = hunter.get_points()
                self._health2 = hunter.get_health()

        #Init the banner message values
        self.set_text(f'Player 1 Score: {self._score1}                             Player 2 Score: {self._score2}\nPlayer 1 Health: {self._health1}                          Player 2 Health: {self._health2}\n{self._message}')
        self.set_font_size(constants.FONT_SIZE)
        self.set_color(constants.WHITE)
        self.set_position(Point(constants.CELL_SIZE, 0))
