from random import randint
import pygame
from snake import Snake
from levels import get_level
from objects.wall import Wall
from objects.food import Food
from objects.grass import Grass


class LevelHandler:
    """
    A class for generating a level and managing events
    """

    def __init__(self, level: str, cell_size: int, image_loader: object, score:object):
        self.level = level
        self.level_map = get_level(self.level)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = cell_size
        self.image_loader = image_loader

        self.score = score
        self.snake = None

        self.walls = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.sprite_groups = pygame.sprite.Group()

    def get_sprites(self):
        for y in range(self.display_height):
            for x in range(self.display_width):
                cell = self.level_map[y][x]
                x_pos = self.cell_size * x
                y_pos = self.cell_size * y
                match cell:
                    case 0:
                        self.grass.add(Grass(x_pos, y_pos, self.image_loader))
                    case 1:
                        self.grass.add(Grass(x_pos, y_pos, self.image_loader))
                        self.walls.add(Wall(self.image_loader, x_pos, y_pos))
                    case 2:
                        self.grass.add(Grass(x_pos, y_pos, self.image_loader))
                        self.food.add(Food(x_pos, y_pos, self.cell_size, self.image_loader))
                    case 3:
                        self.grass.add(Grass(x_pos, y_pos, self.image_loader))
                        self.snake = Snake(
                            x,
                            y,
                            self.cell_size,
                            self.display_width,
                            self.display_height
                        )

        self.sprite_groups.add(self.grass, self.walls, self.food)
        return self.sprite_groups

    def increase_score(self):
        self.score.increase()

    def level_score(self):
        return self.score.show()

    def reset_level_score(self):
        self.score.reset()

    def victory(self):
        if self.score.show() > 99:
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
        self.snake.change_direction(direction)

    def snake_move(self):
        self.snake.move_snake()

    def grow_snake(self):
        self.snake.grow_snake()

    def snakes_body(self):
        return self.snake.snakes_body()

    def snakes_current_direction(self):
        return self.snake.snakes_direction()

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
            new_food = Food(x_pos, y_pos, self.cell_size, self.image_loader)

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
        self.grass.empty()
        self.sprite_groups.empty()
        self.snake = None
        self.get_sprites()
