import constants
from game.casting.actor import Actor
from game.casting.hunter import Hunter
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with another cycle, or the cycle collides with its trails, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._current_score = 0
        self._message_counter = 0

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
                banner.set_text('')
    
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
        """Sets the game over flag if the cycle collides with one of its or another players trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        hunters = cast.get_actors("hunters")
        banner = cast.get_first_actor("banners")
        treasures = cast.get_actors("treasures")
        score = cast.get_first_actor("score")


        for j in treasures:
            for hunter in hunters:
                #show treasure and increase score of hunter if collision is found
                if j.get_position().equals(hunter.get_position()):
                    color = Color(255, 255, 255)
                    j.set_color(color)
                    message = j.get_message()
                    banner.set_text(message)
                    self._current_score += 1
                    score.add_points(self._current_score)
                    self._message_counter += 1


    def _handle_trap_collision(self, cast):
        """Updates the score and if a player collides with a light trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        hunters = cast.get_actors("hunters")
        banner = cast.get_first_actor("banners")
        traps = cast.get_actors("traps")
        health = cast.get_first_actor("health")

        for k in traps:
            for hunter in hunters:
                #show trap and decrease hunter health if collision is found
                if k.get_position().equals(hunter.get_position()):
                    color = Color(255, 0, 0)
                    k.set_color(color)
                    if k.get_damage != 0:
                        banner.set_text('You took damage from a trap')
                        k.set_damage(50)
                        hp = -50
                        health.add_health(hp)
                        self._message_counter += 1
                    elif k.get_damage == 0:
                        banner.set_text('This trap has been activated already')
                        self._message_counter += 1


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles to white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        if self._is_game_over:
            hunter = cast.get_first_actor("Hunter")
            score = cast.get_first_actor("score")



            message = Actor()
            message.set_text(f"Game Over!")
            cast.add_actor("messages", message)