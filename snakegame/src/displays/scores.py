import pygame


class HighScoreScreen:
    def __init__(self, display, level_map):
        self._display = display
        self._width = len(level_map[0])
        self._height = len(level_map)
        self._font = pygame.font.SysFont("arialblack", 45)
        self._small_font = pygame.font.SysFont("arialblack", 25)

    def draw(self, high_scores):
        self._display.fill((55, 174, 15))
        position_y = 130
        text = self._font.render("High Scores", True, (0, 0, 0))
        text_rect = text.get_rect(center=((self._width * 30) // 2, 100))
        self._display.blit(text, text_rect)

        for score in high_scores:
            position_y += 30
            text = self._small_font.render(str(score), True, (0, 0, 0))
            text_rect = text.get_rect(center=((self._width * 30) // 2, position_y))
            self._display.blit(text, text_rect)

        text = self._small_font.render("Esc : back to main menu", True, (0, 0, 0))
        text_rect = text.get_rect(center=((self._width * 30) // 2, position_y + 50))
        self._display.blit(text, text_rect)
