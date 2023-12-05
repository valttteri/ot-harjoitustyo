import pygame
from levelhandler import LevelHandler
from levels import get_level
from high_score import HighScore


class GameStateHandler:
    def __init__(self, high_scores:list, level: str, renderer: object):
        self.new_state = None
        self.high_scores = high_scores
        self.level = level
        self.level_map = get_level(self.level)
        self.cell_size = 30

        self.renderer = renderer
        self.level_handler = LevelHandler(self.level_map, self.cell_size)
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
        self.renderer.display_score(
            self.level_handler.score.show(), 26 * self.cell_size, 1.5 * self.cell_size
        )

        food_consumed = self.level_handler.snake_eats_food()
        if food_consumed:
            self.level_handler.relocate_food(food_consumed[0])
            self.level_handler.snake.grow_snake()
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
        for i, part in enumerate(self.level_handler.snake.snakes_body()):
            if i == 0:
                self.renderer.render_snakes_head(
                    part, self.level_handler.snake.snakes_direction()
                )
            elif i == len(self.level_handler.snake.snakes_body()) - 1:
                self.renderer.render_snakes_tail(
                    part, self.level_handler.snake.snakes_body()[i - 1]
                )
            else:
                self.renderer.render_snakes_body(
                    part,
                    self.level_handler.snake.snakes_body()[i - 1],
                    self.level_handler.snake.snakes_body()[i + 1],
                )

    def save_final_score(self):
        final_score = HighScore(self.level_handler.level_score(), "Mikko")
        self.high_scores.append(final_score)
        self.level_handler.reset_level_score()
