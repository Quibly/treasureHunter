import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color
from constants import DEFAULT_TREASURES
from constants import WHITE
from constants import YELLOW
from constants import GREEN
from constants import RED

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the hunter collides
    with a treasure or trap, or if the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._message_counter = 0
        self._treasures_found = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        banner = cast.get_first_actor("banners")

        if not self._is_game_over:
            self._message_counter = 0
            self._handle_ground_cover_collision(cast)
            self._handle_treasure_collision(cast)
            self._handle_trap_collision(cast)
            self._handle_game_over(cast)
            if self._message_counter == 0:
                banner.set_message('')
                banner.display_banner()

    def get_game_over(self):
        """
        """
        return self._is_game_over
    
    def _handle_ground_cover_collision(self, cast):
        """Updates the score and if a player collides with a light trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        hunters = cast.get_actors("hunters")
        ground_covers = cast.get_actors("ground_covers")

        for i in ground_covers:
            for hunter in hunters:
                #remove ground_cover when collisions are found
                if i.get_position().equals(hunter.get_position()):
                    i.set_display_toggle(0)
            if i.get_display_toggle() == 0:
                cast.remove_actor("ground_covers", i)

                  
        
    def _handle_treasure_collision(self, cast):
        """Sets the game over flag if the hunter collides with a treasure or trap.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        hunters = cast.get_actors("hunters")
        banner = cast.get_first_actor("banners")
        treasures = cast.get_actors("treasures")


        for treasure in treasures:
            for hunter in hunters:
                #show treasure and increase score of hunter if collision is found
                if treasure.get_position().equals(hunter.get_position()):
                    treasure.set_color(GREEN)
                    message = treasure.get_message()
                    points = treasure.get_value()
                    banner.set_message(message)
                    #check for player number and assign points gain to appropriate player
                    if hunter.get_player_number() == 1:
                        banner.set_treasure_gain1(points)
                    elif hunter.get_player_number() ==2:
                        banner.set_treasure_gain2(points)
                    if treasure.get_value() != 0:
                        self._treasures_found += 1
                    banner.display_banner()
                    #set treasure value to 0 for additional collisions
                    treasure.set_value(0)
                    self._message_counter += 1
                    


    def _handle_trap_collision(self, cast):
        """Updates the score and if a player collides with a light trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        hunters = cast.get_actors("hunters")
        banner = cast.get_first_actor("banners")
        traps = cast.get_actors("traps")

        for trap in traps:
            for hunter in hunters:
                #show trap and decrease hunter health if collision is found
                if trap.get_position().equals(hunter.get_position()):
                    trap.set_color(RED)
                    damage = trap.get_damage()
                    if damage != 0:
                        banner.set_message('You took damage from a trap')
                        if hunter.get_player_number() == 1:
                            banner.set_trap_damage1(damage)
                        elif hunter.get_player_number() == 2:
                            banner.set_trap_damage2(damage)
                        banner.display_banner()
                        trap.set_damage(0)
                        self._message_counter += 1
                    elif damage == 0:
                        banner.set_message('This trap has been activated already')
                        banner.display_banner()
                        self._message_counter += 1


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the baord to white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        banner = cast.get_first_actor("banners")
        health1 = banner.get_health1()
        health2 = banner.get_health2()
        ground_covers = cast.get_actors("ground_covers")

        if self._treasures_found == DEFAULT_TREASURES:
            self._is_game_over = True
        elif health1 <= 0:
            self._is_game_over = True
        elif health2 <= 0:
            self._is_game_over = True

        if self._is_game_over:

            x = 600 #int(constants.MAX_X / 2)
            y = 30 #int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_color(YELLOW)
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for ground_cover in ground_covers:
                ground_cover.set_color(WHITE)
