import pygame
from levelhandler import LevelHandler
from displays.start import StartScreen
from displays.pause import PauseScreen
from displays.game_over import GameOverScreen
from displays.victory import VictoryScreen
from displays.scores import HighScoreScreen
from levels import get_level
from high_score import HighScore


class GameStateHandler:
    def __init__(self, level: str):
        pygame.init()
        self.new_state = None
        self.high_scores = []
        self.level = level
        self.level_map = get_level(self.level)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30
        self.display = pygame.display.set_mode(
            (self.cell_size * self.display_width, self.cell_size * self.display_height)
        )
        pygame.display.set_caption("Snake 2023")

        self.score_font = pygame.font.SysFont("Arial", 24)

        self.level_handler = LevelHandler(self.level_map, self.cell_size)
        self.level_sprites = self.level_handler.get_sprites()

        self.start_screen = StartScreen(self.display, self.level_map)
        self.pause_screen = PauseScreen(self.display, self.level_map)
        self.game_over_screen = GameOverScreen(self.display, self.level_map)
        self.victory_screen = VictoryScreen(self.display, self.level_map)
        self.high_score_screen = HighScoreScreen(
            self.display, self.level_map, self.high_scores
        )

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
            case "victory":
                self.victory_screen.draw()
            case "high_score":
                self.high_score_screen.draw()

    def change_state(self):
        return self.new_state

    def reset_state(self):
        self.new_state = None

    def reset_score(self):
        self.level_handler.reset_level_score()

    def get_game_events(self):
        if self.level_handler.snake_collision():
            self.new_state = "game_over"
        if self.level_handler.victory():
            self.new_state = "victory"
        self.plot_sprites()
        self.display_score(26 * self.cell_size, 1.5 * self.cell_size)

        food_consumed = self.level_handler.snake_eats_food()
        if food_consumed:
            self.level_handler.relocate_food(food_consumed[0])
            self.level_handler.snake.grow_snake()
            self.level_handler.increase_score()

    def plot_sprites(self):
        self.display.fill((0, 216, 58))
        self.level_sprites.draw(self.display)
        self.plot_snake()


    def plot_snake(self):
        for i, part in enumerate(self.level_handler.snake.snakes_body()):
            if i == 0:
                self.plot_snakes_head(part)
            elif i == len(self.level_handler.snake.snakes_body()) - 1:
                self.plot_snakes_tail(
                    part, self.level_handler.snake.snakes_body()[i - 1]
                )
            else:
                self.plot_snakes_body(
                    part,
                    self.level_handler.snake.snakes_body()[i - 1],
                    self.level_handler.snake.snakes_body()[i + 1],
                )

    def plot_snakes_body(self, part, previous_part, next_part):
        """
        Plot each part of the snakes body between its head and tail
        """
        # horizontal and vertical parts
        if previous_part.y == part.y == next_part.y:
            self.display_graphics("snake_body_hz", part.x, part.y)
        elif previous_part.x == part.x == next_part.x:
            self.display_graphics("snake_body_vert", part.x, part.y)

        # when snake turns
        elif (
            part.y == min(previous_part.y, next_part.y)
            and part.x == min(previous_part.x, next_part.x)
        ):
            self.display_graphics("snake_turn_bottom_right", part.x, part.y)
        elif (
            part.y == max(previous_part.y, next_part.y)
            and part.x == max(previous_part.x, next_part.x)
        ):
            self.display_graphics("snake_turn_top_left", part.x, part.y)
        elif (
            part.y == max(previous_part.y, next_part.y)
            and part.x == min(previous_part.x, next_part.x)
        ):
            self.display_graphics("snake_turn_top_right", part.x, part.y)
        elif (
            part.y == min(previous_part.y, next_part.y)
            and part.x == max(previous_part.x, next_part.x)
        ):
            self.display_graphics("snake_turn_bottom_left", part.x, part.y)

    def plot_snakes_tail(self, tail, part_before_tail):
        if part_before_tail.y < tail.y:
            self.display_graphics("snake_tail_down", tail.x, tail.y)
        if part_before_tail.y > tail.y:
            self.display_graphics("snake_tail_up", tail.x, tail.y)
        if part_before_tail.x > tail.x:
            self.display_graphics("snake_tail_left", tail.x, tail.y)
        if part_before_tail.x < tail.x:
            self.display_graphics("snake_tail_right", tail.x, tail.y)

    def plot_snakes_head(self, head):
        direction = self.level_handler.snake.snakes_direction()
        match (direction["x"], direction["y"]):
            case (0, -1):
                self.display_graphics("snake_head_up", head.x, head.y)
            case (0, 1):
                self.display_graphics("snake_head_down", head.x, head.y)
            case (-1, 0):
                self.display_graphics("snake_head_left", head.x, head.y)
            case (1, 0):
                self.display_graphics("snake_head_right", head.x, head.y)

    def display_score(self, x_pos, y_pos):
        text = self.score_font.render(
            f"Score: {self.level_handler.score.show()}", True, (86, 86, 86)
        )
        if self.level_handler.score.show() > 99:
            self.display.blit(text, (x_pos - 15, y_pos))
            return
        self.display.blit(text, (x_pos, y_pos))

    def save_final_score(self):
        final_score = HighScore(self.level_handler.level_score(), "Mikko")
        self.high_scores.append(final_score)
        self.level_handler.reset_level_score()

    def display_graphics(self, name: str, x_pos, y_pos):
        """
        Renders a particular image on screen
        """
        image = pygame.transform.scale(
            pygame.image.load(f"src/images/{name}.png").convert_alpha(), (30, 30)
        )
        self.display.blit(image, (x_pos, y_pos))
