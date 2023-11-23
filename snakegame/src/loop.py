import pygame
from levelhandler import LevelHandler
from levels import get_level


class Loop:
    def __init__(self):
        self.status = "level_one"
        self.cell_size = 30
        self.level_map = get_level(self.status)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.level_generator = LevelHandler(self.level_map)
        self.display = self.level_generator.display
        pygame.display.set_caption("Snake 2023")
        self.clock = pygame.time.Clock()

        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

        self.running = True

    def execute(self):
        while self.running:
            self.get_events()
            self.level_generator.plot_sprites()

            if self.level_generator.snake_collision():
                self.level_generator.snake.reset_snake()
            pygame.display.update()

            self.clock.tick(60)

        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_UP:
                    self.level_generator.snake.change_direction("up")
                if event.key == pygame.K_DOWN:
                    self.level_generator.snake.change_direction("down")
                if event.key == pygame.K_LEFT:
                    self.level_generator.snake.change_direction("left")
                if event.key == pygame.K_RIGHT:
                    self.level_generator.snake.change_direction("right")
                if event.key == pygame.K_g:
                    self.level_generator.snake.grow_snake()
            if event.type == self.MOVE_SNAKE:
                self.level_generator.snake.move_snake()

            elif event.type == pygame.QUIT:
                self.running = False
