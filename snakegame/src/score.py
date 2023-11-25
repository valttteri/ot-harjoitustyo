import pygame

class Score:
    def __init__(self, score=0):
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 24)

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0
    
    def show(self, display, x_pos, y_pos):
        text = self.font.render(f"Score: {self.score}", True, (86, 86, 86))
        display.blit(text, (x_pos, y_pos))