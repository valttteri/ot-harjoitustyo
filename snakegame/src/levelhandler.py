from random import randint
import pygame
from score import Score
from objects.snake import Snake
from objects.wall import Wall
from objects.food import Food

class LevelHandler:
    def __init__(self, level_map: list, cell_size: int):
        self.level_map = level_map
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = cell_size

        self.score = Score(0)
        self.snake = None

        self.walls = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.sprite_groups = pygame.sprite.Group()

    def get_sprites(self):
        for y in range(self.display_height):
            for x in range(self.display_width):
                cell = self.level_map[y][x]
                x_pos = self.cell_size * x
                y_pos = self.cell_size * y
                match cell:
                    case 1:
                        self.walls.add(Wall(x_pos, y_pos))
                    case 2:
                        self.food.add(Food(x_pos, y_pos, self.cell_size))
                    case 3:
                        self.snake = Snake(
                            x,
                            y,
                            self.cell_size,
                            self.display_width,
                            self.display_height,
                        )

        self.sprite_groups.add(self.walls, self.food)
        return self.sprite_groups

    def increase_score(self):
        self.score.increase()
    
    def level_score(self):
        return self.score.show()

    def reset_level_score(self):
        self.score.reset()
    
    def victory(self):
        if self.score.show() > 9:
            self.reset_level()
            return True
        return False

    def snake_collision(self):
        if (
            pygame.sprite.spritecollide(self.snake, self.walls, True)
            or self.snake.snake_hits_itself()
        ):
            self.reset_level()
            return True
        return False

    def snake_eats_food(self):
        return pygame.sprite.spritecollide(self.snake, self.food, False)

    def change_snakes_direction(self, direction: str):
        match direction:
            case "up":
                self.snake.change_direction("up")
            case "down":
                self.snake.change_direction("down")
            case "left":
                self.snake.change_direction("left")
            case "right":
                self.snake.change_direction("right")

    def snake_move(self):
        self.snake.move_snake()

    def relocate_food(self, food: object):
        while True:
            x_pos = randint(1, 29) * self.cell_size
            y_pos = randint(1, 19) * self.cell_size
            new_position = pygame.Rect(
                x_pos,
                y_pos,
                self.cell_size,
                self.cell_size,
            )
            new_food = Food(x_pos, y_pos, self.cell_size)

            if new_position.collidelist(self.snake.body) != -1:
                continue
            if pygame.sprite.spritecollide(new_food, self.walls, False):
                continue

            food.change_position(x_pos, y_pos)
            break

    def reset_level(self):
        self.snake.reset_snake()
        self.walls.empty()
        self.food.empty()
        self.sprite_groups.empty()
        self.snake = None
        self.get_sprites()
