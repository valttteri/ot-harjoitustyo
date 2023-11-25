import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("src/images/wall.png").convert_alpha(), (30, 30)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
