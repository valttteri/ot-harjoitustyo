import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(
        self, head_x: int, head_y: int, cell_size: int, width: int, height: int, display
    ):
        super().__init__()
        self.head_x = head_x
        self.head_y = head_y
        self.cell_size = cell_size
        self.direction_x = 0
        self.direction_y = -1
        self.display = display
        self.max_x_pos = self.cell_size * width
        self.max_y_pos = self.cell_size * height
        self.grow = False
        self.direction_has_changed = False

        self.body = [
            pygame.Rect(
                head_x * self.cell_size,
                head_y * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                head_x * self.cell_size,
                (head_y + 1) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                head_x * self.cell_size,
                (head_y + 2) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
        ]
        self.rect = self.body[0]

    def reset_snake(self):
        self.direction_x = 0
        self.direction_y = -1
        self.body = [
            pygame.Rect(
                self.head_x * self.cell_size,
                self.head_y * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                self.head_x * self.cell_size,
                (self.head_y + 1) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
            pygame.Rect(
                self.head_x * self.cell_size,
                (self.head_y + 2) * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
        ]

    def plot_snake(self):
        for part in self.body:
            pygame.draw.rect(self.display, (0,100,0), part)

    def move_snake(self):
        new_head = pygame.Rect(
            self.body[0].x, self.body[0].y, self.cell_size, self.cell_size
        )
        new_head.move_ip(
            self.cell_size * self.direction_x, self.cell_size * self.direction_y
        )
        if new_head.x < 0:
            new_head = pygame.Rect(
                self.max_x_pos - self.cell_size,
                self.body[0].y,
                self.cell_size,
                self.cell_size,
            )
        if new_head.x >= self.max_x_pos:
            new_head = pygame.Rect(0, self.body[0].y, self.cell_size, self.cell_size)

        if new_head.y < 0:
            new_head = pygame.Rect(
                self.body[0].x,
                self.max_y_pos - self.cell_size,
                self.cell_size,
                self.cell_size,
            )
        if new_head.y >= self.max_y_pos:
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
                if self.direction_y == 1:
                    return
                self.direction_y = -1
                self.direction_x = 0
            case "down":
                if self.direction_y == -1:
                    return
                self.direction_y = 1
                self.direction_x = 0
            case "right":
                if self.direction_x == -1:
                    return
                self.direction_x = 1
                self.direction_y = 0
            case "left":
                if self.direction_x == 1:
                    return
                self.direction_x = -1
                self.direction_y = 0
        self.direction_has_changed = True

    def grow_snake(self):
        self.grow = True

    def snake_hits_itself(self):
        return self.body[0].collidelistall(self.body[1:])

    def rect_list(self):
        return self.body
