from random import randint
import pygame
from levels import get_level
from objects.snake import Snake
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
        """Generates sprite objects based on the level map

        Returns:
            self.sprite_groups: all sprite objects for the level
        """
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
        """
        Increases player's score by one
        """
        self.score.increase()

    def level_score(self):
        """
        Returns players score

        Returns
            self.score.show(): player's score
        """
        return self.score.show()

    def reset_level_score(self):
        """
        Sets player's score to zero
        """
        self.score.reset()

    def victory(self):
        """Checks if the player has won

        Returns:
            True if player has enough points
            False otherwise
        """
        if self.score.show() > 100:
            self.reset_level()
            return True
        return False

    def snake_collision(self):
        """Checks if the snake has collided with it's own body or an obstacle.
        Resets the level if there's a collision

        Returns:
            True if a collision has happened
            False otherwise
        """
        if (
            pygame.sprite.spritecollide(self.snake, self.walls, True)
            or self.snake.snake_hits_itself()
        ):
            self.reset_level()
            return True
        return False

    def snake_eats_food(self):
        """Checks if snake has 'eaten' a cherry

        Returns:
            True if a collision between snake and a food object has happened
            False otherwise
        """
        return pygame.sprite.spritecollide(self.snake, self.food, False)

    def change_snakes_direction(self, direction: str):
        """
        Gives the snake a command to change direction
        """
        self.snake.change_direction(direction)

    def snake_move(self):
        """
        Gives the snake a command to move when the move_snake - user event triggers
        """
        self.snake.move_snake()

    def grow_snake(self):
        """
        Gives the snake a command to grow
        """
        self.snake.grow_snake()

    def snakes_body(self):
        """Returns the snake's body

        Returns:
            self.snake.snakes_body(): the snake's body
        """
        return self.snake.snakes_body()

    def snakes_current_direction(self):
        """Returns the snakes current direction

        Returns:
            self.snake.snakes_direction(): the snake's current direction
        """
        return self.snake.snakes_direction()

    def relocate_food(self, food: object):
        """Moves a food object to a different location when it gets 'eaten' by the snake

        Args:
            food: the food object that was eaten
        """
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
        """
        Resets the level by removing every sprite and then generating them again
        """
        self.snake.reset_snake()
        self.walls.empty()
        self.food.empty()
        self.grass.empty()
        self.sprite_groups.empty()
        self.snake = None
        self.get_sprites()
