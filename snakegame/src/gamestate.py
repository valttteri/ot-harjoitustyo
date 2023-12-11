from datetime import datetime
from high_score import HighScore


class GameStateHandler:
    """
    A class for managing game states. GameStateHandler object gives
    commands to the level handler and renderer
    """

    def __init__(
        self,
        high_scores: list,
        level: str,
        renderer: object,
        level_handler: object,
        database_handler: object,
    ):
        """
        Constructor for the class

        Args:
            high_scores: a list for storing HighScore objects
            level: the name of the current level
            renderer: a tool for rendering graphics
            level_handler: level handler for the current level
            database_handler: a tool for managing the database
        """
        self._new_state = None
        self._high_scores = high_scores
        self._level = level
        self._database_handler = database_handler
        self._renderer = renderer
        self._level_handler = level_handler
        self._level_sprites = self._level_handler.get_sprites()

    def execute_state(self, state):
        """
        Does actions based on the current game state
        """
        match state:
            case "start":
                self._renderer.render_screen("start")
            case "pause":
                self._renderer.render_screen("pause")
            case "game_over":
                self._renderer.render_screen("game_over")
            case "game_on":
                self.get_game_events()
            case "victory":
                self._renderer.render_screen("victory")
            case "high_score":
                self._renderer.render_screen("high_score_screen", self._high_scores)

    def change_state(self):
        """
        If the return value of this function is not None, 
        game loop knows it's time to change the game state
        """
        return self._new_state

    def reset_state(self):
        """
        Resets the game state
        """
        self._new_state = None

    def reset_score(self):
        """
        Resets the player's score
        """
        self._level_handler.reset_level_score()

    def get_game_events(self):
        """
        Get events that happen while the game is running. Change the game state
        when needed and call functions for rendering everything
        """
        if self._level_handler.snake_collision():
            self._new_state = "game_over"
        if self._level_handler.victory():
            self._new_state = "victory"
        self._renderer.render_sprites(self._level_sprites)
        self.plot_snake()
        self._renderer.display_score(self._level_handler.score.show())

        food_consumed = self._level_handler.snake_eats_food()
        if food_consumed:
            self._level_handler.relocate_food(food_consumed[0])
            self._level_handler.grow_snake()
            self._level_handler.increase_score()

    def snake_direction_change(self, direction):
        """
        Gives the level handler commands to change the snake's direction
        """
        match direction:
            case "up":
                self._level_handler.change_snakes_direction("up")
            case "down":
                self._level_handler.change_snakes_direction("down")
            case "left":
                self._level_handler.change_snakes_direction("left")
            case "right":
                self._level_handler.change_snakes_direction("right")

    def snake_move(self):
        """
        Gives the level handler a command to move the snake
        """
        self._level_handler.snake_move()

    def plot_snake(self):
        """
        Handles the snakes generation
        """
        for i, part in enumerate(self._level_handler.snakes_body()):
            if i == 0:
                self._renderer.render_snakes_head(
                    part, self._level_handler.snakes_current_direction()
                )
            elif i == len(self._level_handler.snakes_body()) - 1:
                self._renderer.render_snakes_tail(
                    part, self._level_handler.snakes_body()[i - 1]
                )
            else:
                self._renderer.render_snakes_body(
                    part,
                    self._level_handler.snakes_body()[i - 1],
                    self._level_handler.snakes_body()[i + 1],
                )

    def save_final_score(self):
        """
        Saves the player's score
        """
        final_score = HighScore(
            self._level_handler.level_score(),
            datetime.now().strftime("%d.%m.%Y klo %H:%M"),
        )
        self._high_scores.append(final_score)
        self._high_scores.sort(key=lambda x: x.score, reverse=True)
        if len(self._high_scores) > 10:
            self._high_scores.pop()
        self._level_handler.reset_level_score()

    def get_high_scores(self):
        """
        Get high scores from database
        """
        self._high_scores = self._database_handler.get_high_scores()

    def save_high_scores_to_database(self):
        """
        Save high scores to database when program closes
        """
        self._database_handler.update_database(self._high_scores)
