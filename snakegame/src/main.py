from loop import Loop
from gamestate import GameStateHandler
from levelhandler import LevelHandler
from pygame_events import PygameEvents
from rendering import Renderer
from clock import PygameClock
from user_events import UserEvents


class SnakeGame:
    def __init__(self):
        self.game_state_handler = GameStateHandler(
            [],
            "level_one",
            Renderer("level_one"),
            LevelHandler("level_one", 30)

        )

        self.infinite_loop = Loop(
            "start",
            "level_one",
            PygameEvents(),
            self.game_state_handler,
            PygameClock(60),
            UserEvents()
        )
        self.infinite_loop.execute()

if __name__ == "__main__":
    SnakeGame()
