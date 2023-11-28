import pygame
from levelhandler import LevelHandler
from displays.start import StartScreen
from displays.pause import PauseScreen
from displays.game_over import GameOverScreen
from levels import get_level


class GameStateHandler:
    def __init__(self):
        self.level = "level_one"
        self.new_state = None
        self.quit = False

        self.level_map = get_level(self.level)
        self.display_width = len(self.level_map[0])
        self.display_height = len(self.level_map)
        self.cell_size = 30
        self.font = pygame.font.SysFont("Arial", 35)
        self.display = pygame.display.set_mode(
            (self.cell_size * self.display_width, self.cell_size * self.display_height)
        )

        self.level_handler = LevelHandler(self.level_map)
        self.start_screen = StartScreen(self.display, self.level_map)
        self.pause_screen = PauseScreen(self.display, self.level_map)
        self.game_over_screen = GameOverScreen(self.display, self.level_map)
        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

    def execute_state(self, state):
        if state == "start":
            self.start()
        if state == "pause":
            self.pause()
        if state == "game_over":
            self.game_over()
        if state == "game_on":
            self.game_on()

    def change_state(self):
        return self.new_state

    def reset_state(self):
        self.new_state = None

    def quit_game(self):
        return self.quit

    def start(self):
        self.start_screen.draw()
        self.start_keys_pressed()

    def game_on(self):
        self.get_game_events()
        self.game_keys_pressed()

    def pause(self):
        self.pause_screen.draw()
        self.pause_keys_pressed()

    def game_over(self):
        self.game_over_screen.draw()
        self.game_over_keys_pressed()

    def start_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                else:
                    self.new_state = "game_on"
            elif event.type == pygame.QUIT:
                self.quit = True

    def pause_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                if event.key == pygame.K_p:
                    self.new_state = "game_on"
            elif event.type == pygame.QUIT:
                self.quit = True

    def game_over_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit = True
                if event.key == pygame.K_1:
                    self.new_state = "game_on"
                if event.key == pygame.K_2:
                    self.new_state = "start"
            elif event.type == pygame.QUIT:
                self.quit = True

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
                    self.quit = True
                if event.key == pygame.K_UP:
                    self.level_handler.snake.change_direction("up")
                if event.key == pygame.K_DOWN:
                    self.level_handler.snake.change_direction("down")
                if event.key == pygame.K_LEFT:
                    self.level_handler.snake.change_direction("left")
                if event.key == pygame.K_RIGHT:
                    self.level_handler.snake.change_direction("right")
                if event.key == pygame.K_p:
                    self.new_state = "pause"
            if event.type == self.move_snake:
                self.level_handler.snake.move_snake()

            elif event.type == pygame.QUIT:
                self.quit = True

    def snake_collision_check(self):
        if self.level_handler.snake_collision():
            self.new_state = "game_over"
