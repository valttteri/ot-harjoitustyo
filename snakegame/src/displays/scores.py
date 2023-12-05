import pygame


class HighScoreScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.width = len(level_map[0])
        self.height = len(level_map)
        self.small_font = pygame.font.SysFont("Arial", 28)
        self.font = pygame.font.SysFont("Arial", 35)

    def draw(self, high_scores):
        self.display.fill((0, 100, 200))
        position_y = 120
        text = self.font.render("High Scores", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                100,
            ),
        )

        for score in high_scores:
            position_y += 30
            text = self.small_font.render(str(score), True, (0, 0, 0))
            self.display.blit(
                text,
                (
                    (self.width * 30) // 2 - 130,
                    position_y,
                ),
            )

        text = self.small_font.render("1 : back to main menu", True, (0, 0, 0))
        self.display.blit(
            text,
            (
                (self.width * 30) // 2 - 130,
                position_y + 30,
            ),
        )
