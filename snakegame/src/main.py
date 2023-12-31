from loop import Loop
from gamestate import GameStateHandler
from levelhandler import LevelHandler
from pygame_events import PygameEvents
from rendering import Renderer
from clock import PygameClock
from user_events import UserEvents
from image_loader import ImageLoader
from objects.score import Score
from database_handler import DatabaseHandler


class SnakeGame:
    """
    Initializes the game loop and starts the game.
    """

    def __init__(self):
        self._database_handler = DatabaseHandler("score_data.db")
        self._level_handler = LevelHandler("level_one", 30, ImageLoader(), Score(0))
        self._game_state_handler = GameStateHandler(
            [],
            "level_one",
            Renderer("level_one", ImageLoader()),
            self._level_handler,
            self._database_handler,
        )

        self._infinite_loop = Loop(
            "start",
            "level_one",
            PygameEvents(),
            self._game_state_handler,
            PygameClock(60),
            UserEvents(),
        )
        self._infinite_loop.execute()


if __name__ == "__main__":
    SnakeGame()
