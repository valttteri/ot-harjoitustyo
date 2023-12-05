import pygame


class UserEvents:
    def __init__(self):
        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

    def time_to_move_snake(self):
        return self.move_snake
