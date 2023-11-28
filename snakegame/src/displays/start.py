import pygame


class StartScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.width = len(level_map[0])
        self.height = len(level_map)
        self.font = pygame.font.SysFont("Arial", 35)

    def draw(self):
        self.display.fill((0, 100, 200))
        text = self.font.render("Press any key to start", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 100,
                (self.height * 30) // 2 - 50,
            ),
        )
