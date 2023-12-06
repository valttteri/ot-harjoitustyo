import pygame


class Loop:
    """
    The game loop. Reacts to keys being pressed and gives commands to game state handler.
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
        self.state = state
        self.level = level

        self.game_state_handler = game_state_handler
        self.events = events
        self.clock = clock

        self.user_events = user_events

        self.running = True

    def execute(self, stop=False):
        self.game_state_handler.get_high_scores()
        while self.running:
            self.game_state_handler.execute_state(self.state)

            new_state = self.game_state_handler.change_state()
            if new_state:
                self.state = new_state
                self.game_state_handler.reset_state()

            match self.state:
                case "start":
                    self.start_keys_pressed()
                case "pause":
                    self.pause_keys_pressed()
                case "game_over":
                    self.game_over_keys_pressed()
                case "victory":
                    self.game_over_keys_pressed()
                case "game_on":
                    self.game_keys_pressed()
                case "high_score":
                    self.high_score_keys_pressed()

            self.events.update_display()
            self.clock.tick()

            if stop:
                break

        self.game_state_handler.save_high_scores_to_database()
        self.events.quit()

    def game_keys_pressed(self):
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_UP:
                    self.game_state_handler.snake_direction_change("up")
                if event.key == pygame.K_DOWN:
                    self.game_state_handler.snake_direction_change("down")
                if event.key == pygame.K_LEFT:
                    self.game_state_handler.snake_direction_change("left")
                if event.key == pygame.K_RIGHT:
                    self.game_state_handler.snake_direction_change("right")
                if event.key == pygame.K_p:
                    self.state = "pause"
            if event.type == self.user_events.time_to_move_snake():
                self.game_state_handler.snake_move()

            elif event.type == pygame.QUIT:
                self.running = False

    def start_keys_pressed(self):
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_1:
                    self.state = "game_on"
                if event.key == pygame.K_2:
                    self.state = "high_score"
                if event.key == pygame.K_3:
                    self.running = False
            elif event.type == pygame.QUIT:
                self.running = False

    def pause_keys_pressed(self):
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_p:
                    self.state = "game_on"
            elif event.type == pygame.QUIT:
                self.running = False

    def game_over_keys_pressed(self):
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_1:
                    self.game_state_handler.reset_score()
                    self.state = "game_on"
                if event.key == pygame.K_2:
                    self.game_state_handler.reset_score()
                    self.state = "start"
                if event.key == pygame.K_3:
                    self.game_state_handler.save_final_score()
                    self.state = "start"
            elif event.type == pygame.QUIT:
                self.running = False

    def high_score_keys_pressed(self):
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_1:
                    self.state = "start"
            elif event.type == pygame.QUIT:
                self.running = False
