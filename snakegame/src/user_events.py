import pygame


class UserEvents:
    """
    Class for managing pygame userevents
    """
    def __init__(self):
        self.move_snake = pygame.USEREVENT
        pygame.time.set_timer(self.move_snake, 200)

    def time_to_move_snake(self):
        """
        This function handles the timing for moving the snake
    
        Returns:
            True if it's been 200 milliseconds since the last time the snake moved
        """
        return self.move_snake
