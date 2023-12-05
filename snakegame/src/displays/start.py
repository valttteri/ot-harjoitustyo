import pygame


class StartScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.width, self.height = len(level_map[0]), len(level_map)
        self.font = pygame.font.SysFont("Arial", 35)
        self.small_font = pygame.font.SysFont("Arial", 28)

    def draw(self):
        self.display.fill((0, 100, 200))
        text = self.font.render("Welcome to Snake 2023", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 - 50,
            ),
        )
        text = self.small_font.render("1 : Start", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 - 10,
            ),
        )
        text = self.small_font.render("2 : High Scores", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 + 20,
            ),
        )
        text = self.small_font.render("3 : Exit", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 + 50,
            ),
        )
