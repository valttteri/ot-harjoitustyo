import pygame


class Grass(pygame.sprite.Sprite):
    """
    Class for creating grass objects
    """
    def __init__(self, x_pos: int, y_pos: int, image_loader):
        """
        Constructor for the class

        Args:
        x_pos: x-coordinate
        y_pos: y-coordinate
        image_loader: tool for loading an image
        """
        super().__init__()
        self.image = image_loader.load_image("grass.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
