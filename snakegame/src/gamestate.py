import pygame
from levelhandler import LevelHandler
from displays.start import StartScreen
from displays.pause import PauseScreen
from displays.game_over import GameOverScreen
from levels import get_level


class GameStateHandler:
    def __init__(self, level: str):
        self.new_state = None

        self.level = level
        self.level_map = get_level(self.level)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30
        self.display = pygame.display.set_mode(
            (self.cell_size * self.display_width, self.cell_size * self.display_height)
        )
        self.score_font = pygame.font.SysFont("Arial", 24)

        self.level_handler = LevelHandler(self.level_map, self.cell_size)
        self.level_sprites = self.level_handler.get_sprites()

        self.start_screen = StartScreen(self.display, self.level_map)
        self.pause_screen = PauseScreen(self.display, self.level_map)
        self.game_over_screen = GameOverScreen(self.display, self.level_map)

    def execute_state(self, state):
        match state:
            case "start":
                self.start_screen.draw()
            case "pause":
                self.pause_screen.draw()
            case "game_over":
                self.game_over_screen.draw()
            case "game_on":
                self.get_game_events()

    def change_state(self):
        return self.new_state

    def reset_state(self):
        self.new_state = None

    def get_game_events(self):
        if self.level_handler.snake_collision():
            self.new_state = "game_over"
        self.plot_sprites()
        self.display_score(26 * self.cell_size, 1.5 * self.cell_size)

        food_consumed = self.level_handler.snake_eats_food()
        if food_consumed:
            self.level_handler.relocate_food(food_consumed[0])
            self.level_handler.snake.grow_snake()
            self.level_handler.increase_score()

    def plot_sprites(self):
        self.display.fill((0, 216, 58))
        self.plot_snake()
        self.level_sprites.draw(self.display)

    def plot_snake(self):
        for part in self.level_handler.snake.snakes_body():
            pygame.draw.rect(self.display, (0, 100, 0), part)

    def display_score(self, x_pos, y_pos):
        text = self.score_font.render(
            f"Score: {self.level_handler.score.show()}", True, (86, 86, 86)
        )
        if self.level_handler.score.show() > 99:
            self.display.blit(text, (x_pos - 15, y_pos))
            return
        self.display.blit(text, (x_pos, y_pos))
