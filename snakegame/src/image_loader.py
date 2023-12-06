import pygame

class ImageLoader:
    def load_image(self, name: str):
        return pygame.transform.scale(
            pygame.image.load(f"src/images/{name}").convert_alpha(), (30, 30)
        )
