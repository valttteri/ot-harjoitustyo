import pygame


class StartScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.width = len(level_map[0])
        self.height = len(level_map)
        self.font = pygame.font.SysFont("Arial", 35)

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
        text = self.font.render("1 : Start", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 - 10,
            ),
        )
        text = self.font.render("2 : High Scores", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 + 30,
            ),
        )
        text = self.font.render("3 : Exit", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                (self.height * 30) // 2 + 70,
            ),
        )
