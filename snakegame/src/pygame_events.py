import pygame


class PygameEvents:
    """
    A class for fetching pygame events
    """
    def get_events(self):
        """
        Returns all pygame events
        """
        return pygame.event.get()

    def update_display(self):
        """
        Updates the pygame display
        """
        pygame.display.update()

    def quit(self):
        """
        Closes the program
        """
        pygame.quit()
