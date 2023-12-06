import pygame


class Grass(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int, image_loader):
        super().__init__()
        self.image = image_loader.load_image("grass.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
