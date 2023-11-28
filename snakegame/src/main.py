import pygame
from loop import Loop


class SnakeGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake 2023")
        
        self.infinite_loop = Loop()
        self.infinite_loop.execute()

if __name__ == "__main__":
    SnakeGame()
