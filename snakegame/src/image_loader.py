import pygame

class ImageLoader:
    """
    Loads game graphics
    """
    def load_image(self, name: str):
        """
        Render an image

        Args:
            name: the image's name
        """
        return pygame.transform.scale(
            pygame.image.load(f"src/images/{name}").convert_alpha(), (30, 30)
        )
