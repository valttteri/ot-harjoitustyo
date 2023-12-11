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
        self._clock = pygame.time.Clock()
        self._fps = fps

    def tick(self):
        """
        Tick the clock
        """
        self._clock.tick(self._fps)
