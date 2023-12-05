import pygame


class GameOverScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.height = len(level_map)
        self.width = len(level_map[0])
        self.font = pygame.font.SysFont("Arial", 35)
        self.small_font = pygame.font.SysFont("Arial", 28)

    def draw(self):
        self.display.fill((200, 200, 200))
        text = self.font.render("Game over!", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 100,
                (self.height * 30) // 2 - 50,
            ),
        )

        text = self.small_font.render("1 : New game", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 100,
                (self.height * 30) // 2 - 10,
            ),
        )

        text = self.small_font.render("2 : Main menu", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 100,
                (self.height * 30) // 2 + 20,
            ),
        )

        text = self.small_font.render("3 : Submit score", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 100,
                (self.height * 30) // 2 + 50,
            ),
        )
