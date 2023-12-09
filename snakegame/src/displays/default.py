import pygame


class DefaultScreen:
    def __init__(self, display, level_map):
        self.display = display
        self.height = len(level_map)
        self.width = len(level_map[0])
        self.font = pygame.font.SysFont("arialblack", 45)
        self.small_font = pygame.font.SysFont("arialblack", 28)

    def get_colour(self, screen_type):
        colours = {
            "game_over": (200, 200, 200),
            "start": (0, 100, 200),
            "victory": (212, 175, 55),
            "pause": (255, 100, 50),
        }
        return colours[screen_type]

    def get_messages(self, screen_type):
        messages = {
            "game_over": [
                "Game over!",
                "1: New game",
                "2 : Main menu",
                "3 : Submit score",
            ],
            "start": [
                "Snake Game 2023",
                "1 : Start",
                "2 : High Scores",
                "3 : Exit",
            ],
            "victory": ["You win!", "1: New game", "2 : Main menu", "3 : Submit score"],
            "pause": ["Paused", "p : continue"],
        }
        return messages[screen_type]

    def draw(self, screen_type):
        text_center = [
            (self.width * 30) // 2,
            (self.height * 30) // 2 - 100,
        ]
        self.display.fill(self.get_colour(screen_type))
        text_topleft = [0, 0]

        for i, message in enumerate(self.get_messages(screen_type)):
            if i == 0:
                text = self.font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=text_center)
                self.display.blit(text, text_rect)
                text_center[1] += 60
                continue

            elif i == 1:
                text = self.small_font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=text_center)
                text_topleft = [text_rect.topleft[0], text_rect.topleft[1]]
                self.display.blit(text, text_rect)
                text_topleft[1] += 30

            else:
                text = self.small_font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(topleft=text_topleft)
                self.display.blit(text, text_rect)
                text_topleft[1] += 30
