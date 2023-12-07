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
        self.new_state = None
        self.high_scores = high_scores
        self.level = level
        self.database_handler = database_handler
        self.renderer = renderer
        self.level_handler = level_handler
        self.level_sprites = self.level_handler.get_sprites()

    def execute_state(self, state):
        match state:
            case "start":
                self.renderer.render_screen("start")
            case "pause":
                self.renderer.render_screen("pause")
            case "game_over":
                self.renderer.render_screen("game_over")
            case "game_on":
                self.get_game_events()
            case "victory":
                self.renderer.render_screen("victory")
            case "high_score":
                self.renderer.render_screen("high_score_screen", self.high_scores)

    def change_state(self):
        """
        Game loop calls this function when it's necessary to change the game state
        """
        return self.new_state

    def reset_state(self):
        self.new_state = None

    def reset_score(self):
        self.level_handler.reset_level_score()

    def get_game_events(self):
        """
        Get events that happen while the game is running. Change the game state
        when needed and call functions for rendering everything
        """
        if self.level_handler.snake_collision():
            self.new_state = "game_over"
        if self.level_handler.victory():
            self.new_state = "victory"
        self.renderer.render_sprites(self.level_sprites)
        self.plot_snake()
        self.renderer.display_score(self.level_handler.score.show())

        food_consumed = self.level_handler.snake_eats_food()
        if food_consumed:
            self.level_handler.relocate_food(food_consumed[0])
            self.level_handler.grow_snake()
            self.level_handler.increase_score()

    def snake_direction_change(self, direction):
        match direction:
            case "up":
                self.level_handler.change_snakes_direction("up")
            case "down":
                self.level_handler.change_snakes_direction("down")
            case "left":
                self.level_handler.change_snakes_direction("left")
            case "right":
                self.level_handler.change_snakes_direction("right")

    def snake_move(self):
        self.level_handler.snake_move()

    def plot_snake(self):
        for i, part in enumerate(self.level_handler.snakes_body()):
            if i == 0:
                self.renderer.render_snakes_head(
                    part, self.level_handler.snakes_current_direction()
                )
            elif i == len(self.level_handler.snakes_body()) - 1:
                self.renderer.render_snakes_tail(
                    part, self.level_handler.snakes_body()[i - 1]
                )
            else:
                self.renderer.render_snakes_body(
                    part,
                    self.level_handler.snakes_body()[i - 1],
                    self.level_handler.snakes_body()[i + 1],
                )

    def save_final_score(self):
        final_score = HighScore(
            self.level_handler.level_score(),
            datetime.now().strftime("%d.%m.%Y klo %H:%M"),
        )
        self.high_scores.append(final_score)
        self.high_scores.sort(key=lambda x: x.score, reverse=True)
        if len(self.high_scores) > 10:
            self.high_scores.pop()
        self.level_handler.reset_level_score()

    def get_high_scores(self):
        """
        Get high scores from database
        """
        self.high_scores = self.database_handler.get_high_scores()

    def save_high_scores_to_database(self):
        """
        Save high scores to database when program closes
        """
        self.database_handler.update_database(self.high_scores)
