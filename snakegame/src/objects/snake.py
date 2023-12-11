import pygame


class Snake(pygame.sprite.Sprite):
    """
    Class for creating food objects
    """

    def __init__(
        self, head_x: int, head_y: int, cell_size: int, width: int, height: int
    ):
        """
        Constructor for the class

        Attributes:
            head_x: x-coordinate of the snake's head
            head_y: y-coordinate of the snake's head
            cell_size: size of the level map's cell
            width: the level map's width
            height: the level map's height
        """
        super().__init__()
        self.cell_size = cell_size
        self.head_pos = {"x": head_x, "y": head_y}
        self.direction = {"x": 0, "y": -1}
        self._max_pos = {"x": self.cell_size * width, "y": self.cell_size * height}
        self.grow = False
        self.direction_has_changed = False

        self.body = self.get_initial_body()
        self.rect = self.body[0]

    def reset_snake(self):
        """
        Moves the snake back to it's starting position and
        reduces the length of it's body back to three
        """
        self.direction["x"] = 0
        self.direction["y"] = -1
        self.body = self.get_initial_body()

    def get_initial_body(self):
        """
        Returns the snakes initial body that has a length of three
        """
        return [
            pygame.Rect(
                self.head_pos["x"] * self.cell_size,
                self.head_pos["y"] * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                self.head_pos["x"] * self.cell_size,
                (self.head_pos["y"] + 1) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                self.head_pos["x"] * self.cell_size,
                (self.head_pos["y"] + 2) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
        ]

    def move_snake(self):
        """
        Moves the snake forward by one length of a cell
        """
        new_head = pygame.Rect(
            self.body[0].x, self.body[0].y, self.cell_size, self.cell_size
        )
        new_head.move_ip(
            self.cell_size * self.direction["x"], self.cell_size * self.direction["y"]
        )
        if new_head.x < 0:
            new_head = pygame.Rect(
                self._max_pos["x"] - self.cell_size,
                self.body[0].y,
                self.cell_size,
                self.cell_size,
            )
        if new_head.x >= self._max_pos["x"]:
            new_head = pygame.Rect(0, self.body[0].y, self.cell_size, self.cell_size)

        if new_head.y < 0:
            new_head = pygame.Rect(
                self.body[0].x,
                self._max_pos["y"] - self.cell_size,
                self.cell_size,
                self.cell_size,
            )
        if new_head.y >= self._max_pos["y"]:
            new_head = pygame.Rect(self.body[0].x, 0, self.cell_size, self.cell_size)

        self.body.insert(0, new_head)
        self.rect = new_head

        if self.grow:
            self.grow = False
        else:
            self.body.pop()
        self.direction_has_changed = False

    def change_direction(self, direction: str):
        """
        Changes the snake's direction

        Args:
            direction: the new direction
        """
        if self.direction_has_changed:
            return
        match direction:
            case "up":
                if self.direction["y"] == 1:
                    return
                self.direction["y"] = -1
                self.direction["x"] = 0
            case "down":
                if self.direction["y"] == -1:
                    return
                self.direction["y"] = 1
                self.direction["x"] = 0
            case "right":
                if self.direction["x"] == -1:
                    return
                self.direction["x"] = 1
                self.direction["y"] = 0
            case "left":
                if self.direction["x"] == 1:
                    return
                self.direction["x"] = -1
                self.direction["y"] = 0
        self.direction_has_changed = True

    def grow_snake(self):
        """
        Sets self.grow true if snake should grow next
        """
        self.grow = True

    def snake_hits_itself(self):
        """
        Return true if snake collides with it's own body
        """
        return self.body[0].collidelistall(self.body[1:])

    def snakes_body(self):
        """
        Returns the snake's current body
        """
        return self.body

    def snakes_direction(self):
        """
        Returns the snake's current direction
        """
        return self.direction
