import pygame
from score import Score
from objects.snake import Snake
from objects.wall import Wall
from objects.food import Food
from random import randint


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
        self.snake = Snake(
            10, 6, self.cell_size, self.display_width, self.display_height, self.display
        )
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

        self.sprite_groups.add(self.walls, self.food)

    def plot_sprites(self):
        self.display.fill((0, 255, 0))
        self.snake.plot_snake()
        self.sprite_groups.draw(self.display)
    
    def update_score(self):
        self.score.show(self.display, 26*self.cell_size, 2*self.cell_size)
    
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
            x_pos = randint(1, 29) * 30
            y_pos = randint(1, 19) * 30
            food.change_position(x_pos, y_pos)

            if pygame.sprite.collide_rect(food, self.snake):
                continue
            if pygame.sprite.spritecollide(food, self.walls, False):
                continue
            break
