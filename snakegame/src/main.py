import pygame
from loop import Loop
from pygame_events import PygameEvents


class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake 2023")
        self.events = PygameEvents()
        self.infinite_loop = Loop("start", self.events)
        self.infinite_loop.execute()


if __name__ == "__main__":
    SnakeGame()
