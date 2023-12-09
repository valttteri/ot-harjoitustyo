import pygame


class DefaultScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.height = len(level_map)
        self.width = len(level_map[0])
        self.font = pygame.font.SysFont("Arial", 35)
        self.small_font = pygame.font.SysFont("Arial", 28)

    def draw(self, screen_type):
        text_y_pos = 50

        colours = {
            "game_over": (200, 200, 200),
            "start": (0, 100, 200),
            "victory": (212, 175, 55),
            "pause": (255, 100, 50),
        }

        messages = {
            "game_over": [
                "Game over!",
                "1: New game",
                "2 : Main menu",
                "3 : Submit score",
            ],
            "start": [
                "Welcome to Snake 2023",
                "1 : Start",
                "2 : High Scores",
                "3 : Exit",
            ],
            "victory": ["You win!", "1: New game", "2 : Main menu", "3 : Submit score"],
            "pause": ["Paused", "p : continue"],
        }

        self.display.fill(colours[screen_type])

        for i, message in enumerate(messages[screen_type]):
            if i == 0:
                text = self.font.render(message, True, (0, 0, 0))
                self.display.blit(
                    text,
                    (
                        (self.width * 30) // 2 - 100,
                        (self.height * 30) // 2 - text_y_pos,
                    ),
                )
                text_y_pos -= 40
            else:
                text = self.small_font.render(message, True, (0, 0, 0))
                self.display.blit(
                    text,
                    (
                        (self.width * 30) // 2 - 100,
                        (self.height * 30) // 2 - text_y_pos,
                    ),
                )
                text_y_pos -= 30
