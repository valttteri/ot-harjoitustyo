import pygame
from levelhandler import LevelHandler
from score import Score
from levels import get_level

class Loop:
    def __init__(self):
        self.status = "level_one"
        self.level_map = get_level(self.status)

        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30

        self.level_handler = LevelHandler(self.level_map)
        self.display = self.level_handler.display
        pygame.display.set_caption("Snake 2023")
        self.clock = pygame.time.Clock()

        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

        self.running = True

    def execute(self):
        while self.running:
            self.get_events()
            self.level_handler.plot_sprites()
            self.level_handler.update_score()

            if self.level_handler.snake_collision():
                self.level_handler.snake.reset_snake()
                self.level_handler.score.reset()

            food_consumed = self.level_handler.snake_eats_food()
            if food_consumed:
                self.level_handler.relocate_food(food_consumed[0])
                self.level_handler.snake.grow_snake()
                self.level_handler.increase_score()
            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_UP:
                    self.level_handler.snake.change_direction("up")
                if event.key == pygame.K_DOWN:
                    self.level_handler.snake.change_direction("down")
                if event.key == pygame.K_LEFT:
                    self.level_handler.snake.change_direction("left")
                if event.key == pygame.K_RIGHT:
                    self.level_handler.snake.change_direction("right")
            if event.type == self.move_snake:
                self.level_handler.snake.move_snake()

            elif event.type == pygame.QUIT:
                self.running = False
