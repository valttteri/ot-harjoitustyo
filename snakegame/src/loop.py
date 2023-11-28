import pygame
from levelhandler import LevelHandler
from levels import get_level


class Loop:
    def __init__(self):
        self.state = "start"
        self.level = "level_one"
        self.level_map = get_level(self.level)

        self.level_handler = LevelHandler(self.level_map)
        self.clock = pygame.time.Clock()

        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

        self.running = True

    def execute(self):
        while self.running:
            if self.state == "start":
                self.level_handler.start_screen()
                self.start_keys_pressed()

            if self.state == "game_on":
                self.get_game_events()
                self.game_keys_pressed()

            if self.state == "game_over":
                self.level_handler.game_over_screen()
                self.game_over_keys_pressed()

            if self.state == "pause":
                self.level_handler.pause_screen()
                self.pause_keys_pressed()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def get_game_events(self):
        self.snake_collision_check()
        self.level_handler.plot_sprites()
        self.level_handler.update_score()

        food_consumed = self.level_handler.snake_eats_food()
        if food_consumed:
            self.level_handler.relocate_food(food_consumed[0])
            self.level_handler.snake.grow_snake()
            self.level_handler.increase_score()

    def game_keys_pressed(self):
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
                if event.key == pygame.K_p:
                    self.state = "pause"
            if event.type == self.move_snake:
                self.level_handler.snake.move_snake()

            elif event.type == pygame.QUIT:
                self.running = False

    def game_over_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_1:
                    self.state = "game_on"
                if event.key == pygame.K_2:
                    self.state = "start"
            elif event.type == pygame.QUIT:
                self.running = False

    def pause_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_p:
                    self.state = "game_on"
            elif event.type == pygame.QUIT:
                self.running = False

    def start_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.state = "game_on"
            elif event.type == pygame.QUIT:
                self.running = False

    def snake_collision_check(self):
        if self.level_handler.snake_collision():
            self.state = "game_over"
