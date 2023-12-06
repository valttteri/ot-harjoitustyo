import pygame


class PygameEvents:
    def get_events(self):
        return pygame.event.get()

    def update_display(self):
        pygame.display.update()

    def quit(self):
        pygame.quit()
