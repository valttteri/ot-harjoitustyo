from random import randint
import pygame
from score import Score
from objects.snake import Snake
from objects.wall import Wall
from objects.food import Food


class LevelHandler:
    def __init__(self, level_map):
        self.level_map = level_map
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30
        self.display = pygame.display.set_mode(
            (self.cell_size * self.display_width, self.cell_size * self.display_height)
        )
        self.score = Score()
        self.snake = None

        self.walls = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.sprite_groups = pygame.sprite.Group()
        self.get_sprites()

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
                            self.display,
                        )

        self.sprite_groups.add(self.walls, self.food)

    def plot_sprites(self):
        self.display.fill((0, 216, 58))
        self.snake.plot_snake()
        self.sprite_groups.draw(self.display)

    def update_score(self):
        self.score.show(self.display, 26 * self.cell_size, 1.5 * self.cell_size)

    def increase_score(self):
        self.score.increase()

    def snake_collision(self):
        if pygame.sprite.spritecollide(self.snake, self.walls, False):
            return True
        if self.snake.snake_hits_itself():
            return True
        return False

    def snake_eats_food(self):
        return pygame.sprite.spritecollide(self.snake, self.food, False)

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
