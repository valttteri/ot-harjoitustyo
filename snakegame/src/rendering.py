import pygame
from displays.start import StartScreen
from displays.pause import PauseScreen
from displays.game_over import GameOverScreen
from displays.victory import VictoryScreen
from displays.scores import HighScoreScreen
from levels import get_level


class Renderer:
    def __init__(self, level):
        pygame.init()
        self.level_map = get_level(level)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30
        self.high_scores = []
        self.display = pygame.display.set_mode(
            (self.cell_size * self.display_width, self.cell_size * self.display_height)
        )
        pygame.display.set_caption("Snake 2023")
        self.start_screen = StartScreen(self.display, self.level_map)
        self.pause_screen = PauseScreen(self.display, self.level_map)
        self.game_over_screen = GameOverScreen(self.display, self.level_map)
        self.victory_screen = VictoryScreen(self.display, self.level_map)
        self.high_score_screen = HighScoreScreen(
            self.display, self.level_map
        )
        
        self.score_font = pygame.font.SysFont("Arial", 24)

    
    def render_screen(self, name, high_scores=None):
        options = {
            "start": StartScreen(self.display, self.level_map),
            "pause": PauseScreen(self.display, self.level_map),
            "game_over": GameOverScreen(self.display, self.level_map),
            "victory": VictoryScreen(self.display, self.level_map),
            "high_score_screen": HighScoreScreen(
                self.display, self.level_map
            ) 
        }
        if name == "high_score_screen":
            options[name].draw(high_scores)
        else:
            options[name].draw()
    
    def render_sprites(self, sprites):
        sprites.draw(self.display)
    
    def display_graphics(self, name: str, x_pos, y_pos):
        """
        Renders a particular image on screen
        """
        image = pygame.transform.scale(
            pygame.image.load(f"src/images/{name}.png").convert_alpha(), (30, 30)
        )
        self.display.blit(image, (x_pos, y_pos))
    
    def render_snakes_body(self, part, previous_part, next_part):
        """
        Render each part of the snake's body excluding the head and the tail
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

    def render_snakes_tail(self, tail, part_before_tail):
        """
        Render the snake's tail
        """
        if part_before_tail.y < tail.y:
            self.display_graphics("snake_tail_down", tail.x, tail.y)
        if part_before_tail.y > tail.y:
            self.display_graphics("snake_tail_up", tail.x, tail.y)
        if part_before_tail.x > tail.x:
            self.display_graphics("snake_tail_left", tail.x, tail.y)
        if part_before_tail.x < tail.x:
            self.display_graphics("snake_tail_right", tail.x, tail.y)

    def render_snakes_head(self, head, direction):
        """
        Render the snake's head
        """
        match (direction["x"], direction["y"]):
            case (0, -1):
                self.display_graphics("snake_head_up", head.x, head.y)
            case (0, 1):
                self.display_graphics("snake_head_down", head.x, head.y)
            case (-1, 0):
                self.display_graphics("snake_head_left", head.x, head.y)
            case (1, 0):
                self.display_graphics("snake_head_right", head.x, head.y)
        
    def display_score(self, score, x_pos, y_pos):
        text = self.score_font.render(
            f"Score: {score}", True, (86, 86, 86)
        )
        if score > 99:
            self.display.blit(text, (x_pos - 15, y_pos))
            return
        self.display.blit(text, (x_pos, y_pos))
