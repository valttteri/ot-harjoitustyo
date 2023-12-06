import pygame


class Food(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int, cell_size: int, image_loader):
        super().__init__()
        self.height = cell_size
        self.width = cell_size
        self.image = image_loader.load_image("cherry.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def change_position(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos
