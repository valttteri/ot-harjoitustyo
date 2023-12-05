import pygame


class Grass(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("src/images/grass.png").convert_alpha(),
            (30, 30)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos