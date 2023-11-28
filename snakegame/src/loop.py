import pygame
from gamestate import GameStateHandler
from levels import get_level


class Loop:
    def __init__(self):
        self.state = "start"
        self.level = "level_one"
        self.level_map = get_level(self.level)

        self.game_state_handler = GameStateHandler()
        self.clock = pygame.time.Clock()

        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

        self.running = True

    def execute(self):
        while self.running:
            self.game_state_handler.execute_state(self.state)

            new_state = self.game_state_handler.change_state()
            if new_state:
                self.state = new_state
                self.game_state_handler.reset_state()

            match self.state:
                case "start":
                    self.start_keys_pressed()
                case "pause":
                    self.pause_keys_pressed()
                case "game_over":
                    self.game_over_keys_pressed()
                case "game_on":
                    self.game_keys_pressed()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
    
    def game_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_UP:
                    self.game_state_handler.level_handler.change_snakes_direction("up")
                if event.key == pygame.K_DOWN:
                    self.game_state_handler.level_handler.change_snakes_direction("down")
                if event.key == pygame.K_LEFT:
                    self.game_state_handler.level_handler.change_snakes_direction("left")
                if event.key == pygame.K_RIGHT:
                    self.game_state_handler.level_handler.change_snakes_direction("right")
                if event.key == pygame.K_p:
                    self.state = "pause"
            if event.type == self.move_snake:
                self.game_state_handler.level_handler.snake_move()

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

    def pause_keys_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_p:
                    self.state = "game_on"
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
