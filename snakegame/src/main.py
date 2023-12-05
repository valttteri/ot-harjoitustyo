from loop import Loop
from gamestate import GameStateHandler
from pygame_events import PygameEvents
from rendering import Renderer


class SnakeGame:
    def __init__(self):
        self.events = PygameEvents()
        self.renderer = Renderer("level_one")
        self.game_state_handler = GameStateHandler([], "level_one", self.renderer)
        self.infinite_loop = Loop(
            "start", "level_one", self.events, self.game_state_handler
        )
        self.infinite_loop.execute()


if __name__ == "__main__":
    SnakeGame()
