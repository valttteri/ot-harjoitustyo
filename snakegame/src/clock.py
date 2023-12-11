import pygame


class PygameClock:
    """
    Class for managing the pygame clock
    """
    def __init__(self, fps):
        """
        Constructor for the class

        Args:
            fps: the game's framerate
        """
        self.clock = pygame.time.Clock()
        self.fps = fps

    def tick(self):
        """
        Tick the clock
        """
        self.clock.tick(self.fps)
        
