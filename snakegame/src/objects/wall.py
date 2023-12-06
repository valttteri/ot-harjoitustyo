import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, image_loader, x_pos=0, y_pos=0):
        super().__init__()

        self.image = image_loader.load_image("wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
