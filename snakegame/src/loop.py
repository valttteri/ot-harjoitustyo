import pygame
from levelhandler import LevelHandler
from gamestate import GameStateHandler
from levels import get_level


class Loop:
    def __init__(self):
        self.state = "start"
        self.level = "level_one"
        self.level_map = get_level(self.level)

        self.game_state_handler = GameStateHandler()
        self.clock = pygame.time.Clock()

        self.running = True

    def execute(self):
        while self.running:
            self.game_state_handler.execute_state(self.state)
            
            if self.game_state_handler.quit_game():
                self.running = False
            new_state = self.game_state_handler.change_state()
            if new_state:
                self.state = new_state
                self.game_state_handler.reset_state()
                
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
