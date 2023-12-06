from loop import Loop
from gamestate import GameStateHandler
from levelhandler import LevelHandler
from pygame_events import PygameEvents
from rendering import Renderer
from clock import PygameClock
from user_events import UserEvents
from image_loader import ImageLoader
from score import Score


class SnakeGame:
    """
    Initializes the game loop and starts the game.
    """

    def __init__(self):
        self.level_handler = LevelHandler("level_one", 30, ImageLoader(), Score(0))
        self.game_state_handler = GameStateHandler(
            [], "level_one", Renderer("level_one"), self.level_handler
        )

        self.infinite_loop = Loop(
            "start",
            "level_one",
            PygameEvents(),
            self.game_state_handler,
            PygameClock(60),
            UserEvents(),
        )
        self.infinite_loop.execute()


if __name__ == "__main__":
    SnakeGame()
