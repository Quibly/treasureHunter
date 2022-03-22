from game.shared.color import Color

class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            _current_score : A variable to hold the current score.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        # hunters = cast.get_actors("hunters")
        # velocity = self._keyboard_service.get_direction()
        # for hunter in hunters:
        #     hunter.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position, the artifact positions, and resolves any collisions with artifacts.
           Allows user to pick the level of difficulty in the program.
        
        Args:
            cast (Cast): The cast of actors.
            cols : The COLS specified in __main__
            cell_size: The CELL_SIZE specified in __main__
            difficulty: The difficulty selected in __main__ starting
        """

        # banner = cast.get_first_actor("banners")
        # hunters = cast.get_actors("hunters")
        # treasures = cast.get_actors("treasures")
        # ground_covers = cast.get_actors("ground_covers")
        # traps = cast.get_actors("traps")

        # banner.set_text(f"Score: {self._current_score}")
        # max_x = self._video_service.get_width()
        # max_y = self._video_service.get_height()
        # for hunter in hunters:
        #     hunter.move_next(max_x,max_y)
        # message_counter = 0

        #check for ground cover collisions
        # for i in ground_covers:
        #     for hunter in hunters:
        #         #remove ground_cover when collisions are found
        #         if i.get_position().equals(hunter.get_position()):
        #             i.set_display_toggle(0)
        #     if i.get_display_toggle() == 0:
        #         cast.remove_actor("ground_covers", i)

        # #check for treasure collissions
        # for j in treasures:
        #     for hunter in hunters:
        #         #show treasure and increase score of hunter if collision is found
        #         if j.get_position().equals(hunter.get_position()):
        #             color = Color(255, 255, 255)
        #             j.set_color(color)
        #             message = j.get_message()
        #             banner.set_text(message)
        #             self._current_score += 1
        #             j.set_value(0)
        
        # #check for trap collissions
        # for k in traps:
        #     for hunter in hunters:
        #         #show trap and decrease hunter health if collision is found
        #         if k.get_position().equals(hunter.get_position()):
        #             color = Color(255, 0, 0)
        #             k.set_color(color)
        #             if k.get_damage != 0:
        #                 banner.set_text('You took damage from a trap')
        #                 k.set_damage(0)
        #             elif k.get_damage == 0:
        #                 banner.set_text('This trap has been activated already')
                                       


    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        # self._video_service.clear_buffer()
        # actors = cast.get_all_actors()
        # self._video_service.draw_actors(actors)
        # self._video_service.flush_buffer()
