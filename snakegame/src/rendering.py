import pygame
from displays.default import DefaultScreen
from displays.scores import HighScoreScreen
from levels import get_level


class Renderer:
    """
    A class for rendering all game graphics
    """

    def __init__(self, level: str, image_loader: object):
        """
        Constructor for the class

        Args:
            level: the name of the current level
        """
        pygame.init()
        self.image_loader = image_loader
        self._level_map = get_level(level)
        self._display_width = len(self._level_map[0])
        self._display_height = len(self._level_map)
        self._cell_size = 30
        self._high_scores = []
        self.display = pygame.display.set_mode(
            (self._cell_size * self._display_width, self._cell_size * self._display_height)
        )
        pygame.display.set_caption("Snake 2023")

    def render_screen(self, name, high_scores=None):
        """
        Renders a screen
        """
        if name == "high_score_screen":
            HighScoreScreen(self.display, self._level_map).draw(high_scores)
        else:
            DefaultScreen(self.display, self._level_map).draw(name)

    def render_sprites(self, sprites):
        """
        Renders every sprite of a level
        """
        sprites.draw(self.display)

    def display_graphics(self, name: str, x_pos, y_pos):
        """
        Renders a particular image on screen
        """
        image = self.image_loader.load_image(name)
        self.display.blit(image, (x_pos, y_pos))

    def render_snakes_body(self, part, previous_part, next_part):
        """
        Render each part of the snake's body excluding the head and the tail
        """
        # horizontal and vertical parts
        if previous_part.y == part.y == next_part.y:
            self.display_graphics("snake_body_hz.png", part.x, part.y)
        elif previous_part.x == part.x == next_part.x:
            self.display_graphics("snake_body_vert.png", part.x, part.y)

        # when snake turns
        elif part.y == min(previous_part.y, next_part.y) and part.x == min(
            previous_part.x, next_part.x
        ):
            self.display_graphics("snake_turn_bottom_right.png", part.x, part.y)
        elif part.y == max(previous_part.y, next_part.y) and part.x == max(
            previous_part.x, next_part.x
        ):
            self.display_graphics("snake_turn_top_left.png", part.x, part.y)
        elif part.y == max(previous_part.y, next_part.y) and part.x == min(
            previous_part.x, next_part.x
        ):
            self.display_graphics("snake_turn_top_right.png", part.x, part.y)
        elif part.y == min(previous_part.y, next_part.y) and part.x == max(
            previous_part.x, next_part.x
        ):
            self.display_graphics("snake_turn_bottom_left.png", part.x, part.y)

    def render_snakes_tail(self, tail, part_before_tail):
        """
        Render the snake's tail
        """
        if part_before_tail.y < tail.y:
            self.display_graphics("snake_tail_down.png", tail.x, tail.y)
        if part_before_tail.y > tail.y:
            self.display_graphics("snake_tail_up.png", tail.x, tail.y)
        if part_before_tail.x > tail.x:
            self.display_graphics("snake_tail_left.png", tail.x, tail.y)
        if part_before_tail.x < tail.x:
            self.display_graphics("snake_tail_right.png", tail.x, tail.y)

    def render_snakes_head(self, head, direction):
        """
        Render the snake's head
        """
        match (direction["x"], direction["y"]):
            case (0, -1):
                self.display_graphics("snake_head_up.png", head.x, head.y)
            case (0, 1):
                self.display_graphics("snake_head_down.png", head.x, head.y)
            case (-1, 0):
                self.display_graphics("snake_head_left.png", head.x, head.y)
            case (1, 0):
                self.display_graphics("snake_head_right.png", head.x, head.y)

    def display_score(self, score):
        """
        Renders the player's score
        """
        x_pos = 24 * self._cell_size
        y_pos = 1.5 * self._cell_size
        score_font = pygame.font.SysFont("arialblack", 24)
        text = score_font.render(f"Score: {score}", True, (0, 0, 0))
        self.display.blit(text, (x_pos, y_pos))
