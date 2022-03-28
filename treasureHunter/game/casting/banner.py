from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
import constants
from constants import HUNTER_HEALTH
from constants import TREASURE_VALUE
from constants import TRAP_DAMAGE

class Banner(Actor):
    """
    

    Attributes:
        
    """
    def __init__(self):
        """
        
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
        """
        self._message = message
    
    def set_treasure_gain1(self, points):
        """
        """
        self._score1 = self._score1 + points

    def set_treasure_gain2(self, points):
        """
        """
        self._score2 = self._score2 + points
    
    def set_trap_damage1(self, damage):
        """
        """
        self._health1 = self._health1 - damage

    def set_trap_damage2(self, damage):
        """
        """
        self._health2 = self._health2 - damage

    def get_health1(self):
        """
        """
        return self._health1

    def get_health2(self):
        """
        """
        return self._health2

    def display_banner(self):
        """
        """
        self.set_text(f'Player 1 Score: {self._score1}                             Player 2 Score: {self._score2}\nPlayer 1 Health: {self._health1}                          Player 2 Health: {self._health2}\n{self._message}')

    def _prepare_banner(self):
        """
        """
        cast = Cast()
        
        hunters = cast.get_actors("hunters")
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
