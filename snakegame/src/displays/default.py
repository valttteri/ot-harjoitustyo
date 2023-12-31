import pygame


class DefaultScreen:
    def __init__(self, display, level_map):
        self._display = display
        self._height = len(level_map)
        self._width = len(level_map[0])
        self._font = pygame.font.SysFont("arialblack", 45)
        self._small_font = pygame.font.SysFont("arialblack", 28)

    def get_colour(self, screen_type):
        colours = {
            "game_over": (200, 200, 200),
            "start": (55, 174, 15),
            "victory": (212, 175, 55),
            "pause": (255, 100, 50),
        }
        return colours[screen_type]

    def get_messages(self, screen_type):
        messages = {
            "game_over": [
                "Game over!",
                "1: New game",
                "2 : Submit score",
                "Esc : Main menu",
            ],
            "start": [
                "Snake Game 2023",
                "1 : Start",
                "2 : High Scores",
                "Esc : Exit",
            ],
            "victory": [
                "You win!",
                "1: New game",
                "2 : Submit score",
                "Esc : Main menu",
            ],
            "pause": ["Paused", "p : Continue", "Esc: Main menu"],
        }
        return messages[screen_type]

    def draw(self, screen_type):
        text_center = [
            (self._width * 30) // 2,
            (self._height * 30) // 2 - 100,
        ]
        self._display.fill(self.get_colour(screen_type))
        text_topleft = [0, 0]

        for i, message in enumerate(self.get_messages(screen_type)):
            if i == 0:
                text = self._font.render(message, True, (0, 0, 0))
                text_rect = text.get_rect(center=text_center)
                self._display.blit(text, text_rect)
                text_center[1] += 60
                continue

            text = self._small_font.render(message, True, (0, 0, 0))

            if i == 1:
                text_rect = text.get_rect(center=text_center)
                text_topleft = [text_rect.topleft[0], text_rect.topleft[1]]
            else:
                text_rect = text.get_rect(topleft=text_topleft)

            self._display.blit(text, text_rect)
            text_topleft[1] += 30
