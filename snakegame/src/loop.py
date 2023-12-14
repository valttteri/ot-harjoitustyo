import pygame


class Loop:
    """
    A class for managing the game loop.
    """

    def __init__(
        self,
        state: str,
        level: str,
        events: object,
        game_state_handler: object,
        clock: object,
        user_events: object,
    ):
        """
        Constructor for the class

        Args:
            state: the initial game state
            level: the initial level name
            events: object that returns all pygame events
            game_state_handler: a tool for managing the game states
            clock: the pygame clock
            user_events: returns the pygame userevents
        """
        self.state = state
        self._level = level

        self._game_state_handler = game_state_handler
        self._events = events
        self._clock = clock

        self._user_events = user_events

        self.running = True

    def execute(self, stop=False):
        """
        The main game loop.

        Args:
            stop: False by default. If true, then the game loop stops after the first loop.
                This happens during test runs
        """
        self._game_state_handler.get_high_scores()
        while self.running:
            self._game_state_handler.execute_state(self.state)

            new_state = self._game_state_handler.change_state()
            if new_state:
                self.state = new_state
                self._game_state_handler.reset_state()

            self._keys_pressed()
            self._events.update_display()
            self._clock.tick()

            if stop:
                break

        self._game_state_handler.save_high_scores_to_database()
        self._events.quit()

    def _keys_pressed(self):
        for event in self._events.get_events():
            if event.type == pygame.KEYDOWN:
                match self.state:
                    case "start":
                        self._start_keys_pressed(event)
                    case "pause":
                        self._pause_keys_pressed(event)
                    case "game_over":
                        self._game_over_keys_pressed(event)
                    case "victory":
                        self._game_over_keys_pressed(event)
                    case "game_on":
                        self._game_keys_pressed(event)
                    case "high_score":
                        self._high_score_keys_pressed(event)
            if (
                event.type == self._user_events.time_to_move_snake()
                and self.state == "game_on"
            ):
                self._game_state_handler.snake_move()
            elif event.type == pygame.QUIT:
                self.running = False

    def _game_keys_pressed(self, event):
        """
        User presses a key when in game
        """

        if event.key == pygame.K_ESCAPE:
            self.running = False
        if event.key == pygame.K_UP:
            self._game_state_handler.snake_direction_change("up")
        if event.key == pygame.K_DOWN:
            self._game_state_handler.snake_direction_change("down")
        if event.key == pygame.K_LEFT:
            self._game_state_handler.snake_direction_change("left")
        if event.key == pygame.K_RIGHT:
            self._game_state_handler.snake_direction_change("right")
        if event.key == pygame.K_p:
            self.state = "pause"

    def _start_keys_pressed(self, event):
        """
        User presses a key when in main menu
        """
        if event.key == pygame.K_ESCAPE:
            self.running = False
        if event.key == pygame.K_1:
            self.state = "game_on"
        if event.key == pygame.K_2:
            self.state = "high_score"

    def _pause_keys_pressed(self, event):
        """
        User presses a key when game is paused
        """
        if event.key == pygame.K_ESCAPE:
            self.state = "start"
            self._game_state_handler.reset_score()
        if event.key == pygame.K_p:
            self.state = "game_on"

    def _game_over_keys_pressed(self, event):
        """
        User presses a key when game is over
        """
        if event.key == pygame.K_ESCAPE:
            self.state = "start"
        if event.key == pygame.K_1:
            self._game_state_handler.reset_score()
            self.state = "game_on"
        if event.key == pygame.K_2:
            self._game_state_handler.save_final_score()
            self.state = "start"

    def _high_score_keys_pressed(self, event):
        """
        User presses a key when looking at high scores
        """
        if event.key == pygame.K_ESCAPE:
            self.state = "start"
