import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(
        self, head_x: int, head_y: int, cell_size: int, width: int, height: int
    ):
        super().__init__()
        self.cell_size = cell_size
        self.head_pos = {"x": head_x, "y": head_y}
        self.direction = {"x": 0, "y": -1}
        self.max_pos = {"x": self.cell_size * width, "y": self.cell_size * height}
        self.grow = False
        self.direction_has_changed = False

        self.body = [
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
        self.rect = self.body[0]

    def reset_snake(self):
        self.direction["x"] = 0
        self.direction["y"] = -1
        self.body = [
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
        new_head = pygame.Rect(
            self.body[0].x, self.body[0].y, self.cell_size, self.cell_size
        )
        new_head.move_ip(
            self.cell_size * self.direction["x"], self.cell_size * self.direction["y"]
        )
        if new_head.x < 0:
            new_head = pygame.Rect(
                self.max_pos["x"] - self.cell_size,
                self.body[0].y,
                self.cell_size,
                self.cell_size,
            )
        if new_head.x >= self.max_pos["x"]:
            new_head = pygame.Rect(0, self.body[0].y, self.cell_size, self.cell_size)

        if new_head.y < 0:
            new_head = pygame.Rect(
                self.body[0].x,
                self.max_pos["y"] - self.cell_size,
                self.cell_size,
                self.cell_size,
            )
        if new_head.y >= self.max_pos["y"]:
            new_head = pygame.Rect(self.body[0].x, 0, self.cell_size, self.cell_size)

        self.body.insert(0, new_head)
        self.rect = new_head

        if self.grow:
            self.grow = False
        else:
            self.body.pop()
        self.direction_has_changed = False

    def change_direction(self, direction: str):
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
        self.grow = True

    def snake_hits_itself(self):
        return self.body[0].collidelistall(self.body[1:])

    def snakes_body(self):
        return self.body
