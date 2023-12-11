import pygame


class Food(pygame.sprite.Sprite):
    """
    Class for creating food objects
    """
    def __init__(self, x_pos: int, y_pos: int, cell_size: int, image_loader):
        """
        Constructor for the class
    
        Args:
            x_pos: x-coordinate
            y_pos: y-coordinate
            cell_size: size of the level map's cell 
            image_loader: tool for loading an image
        """
        super().__init__()
        self._height = cell_size
        self._width = cell_size
        self.image = image_loader.load_image("cherry.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def change_position(self, x_pos, y_pos):
        """
        Change the food object's position

            Args:
            x_pos: new x-coordinate
            y_pos: new y-coordinate
        """
        self.rect.x = x_pos
        self.rect.y = y_pos
