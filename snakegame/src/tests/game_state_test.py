import unittest
from gamestate import GameStateHandler
from snake import Snake
from stubs import StubDatabaseHandler


class StubGameEventHandler:
    def __init__(self, level):
        self.level = level

    def reset_score(self):
        print("score was reset")

    def save_final_score(self):
        print("score was submitted")


class StubScreen:
    def __init__(self, screen_type: str):
        self.type = screen_type
        self.status = None

    def draw(self, high_score=None):
        if high_score is not None:
            self.status = f"rendered {self.type} screen with high score {high_score}"
        else:
            self.status = f"rendered {self.type} screen"


class StubRenderer:
    def __init__(self, level):
        self.level = level
        self.stub_screen = None

    def render_screen(self, name, high_scores=None):
        options = {
            "start": StubScreen("start"),
            "pause": StubScreen("pause"),
            "game_over": StubScreen("game_over"),
            "victory": StubScreen("victory"),
            "high_score_screen": StubScreen("high_score"),
        }
        if name == "high_score_screen":
            options[name].draw(high_scores)
        else:
            options[name].draw()
        self.stub_screen = options[name]


class StubLevelHandler:
    def __init__(self, level, cell_size):
        self.level = level
        self.cell_size = cell_size
        self.snake = Snake(6, 6, 30, 30, 20)

    def get_sprites(self):
        return 1

    def change_snakes_direction(self, direction: str):
        self.snake.change_direction(direction)

    def snake_move(self):
        self.snake.move_snake()

    def snakes_current_direction(self):
        return self.snake.snakes_direction()


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.stub_renderer = StubRenderer("level_one")
        self.stub_level_handler = StubLevelHandler("level_one", 30)
        self.game_state_handler = GameStateHandler(
            [1, 2, 3],
            "level_one",
            self.stub_renderer,
            self.stub_level_handler,
            StubDatabaseHandler()
        )

    def test_execute_state(self):
        self.game_state_handler.execute_state("start")
        self.assertEqual(self.stub_renderer.stub_screen.status, "rendered start screen")

        self.game_state_handler.execute_state("pause")
        self.assertEqual(self.stub_renderer.stub_screen.status, "rendered pause screen")

        self.game_state_handler.execute_state("game_over")
        self.assertEqual(
            self.stub_renderer.stub_screen.status, "rendered game_over screen"
        )

        self.game_state_handler.execute_state("victory")
        self.assertEqual(
            self.stub_renderer.stub_screen.status, "rendered victory screen"
        )

        self.game_state_handler.execute_state("high_score")
        self.assertEqual(
            self.stub_renderer.stub_screen.status,
            "rendered high_score screen with high score [1, 2, 3]",
        )

    def test_commanding_snakes_direction(self):
        self.game_state_handler.snake_direction_change("right")
        self.game_state_handler.snake_move()
        self.assertEqual(
            self.stub_level_handler.snakes_current_direction(), {"x": 1, "y": 0}
        )

        self.game_state_handler.snake_direction_change("down")
        self.game_state_handler.snake_move()
        self.assertEqual(
            self.stub_level_handler.snakes_current_direction(), {"x": 0, "y": 1}
        )

        self.game_state_handler.snake_direction_change("left")
        self.game_state_handler.snake_move()
        self.assertEqual(
            self.stub_level_handler.snakes_current_direction(), {"x": -1, "y": 0}
        )

        self.game_state_handler.snake_direction_change("up")
        self.game_state_handler.snake_move()
        self.assertEqual(
            self.stub_level_handler.snakes_current_direction(), {"x": 0, "y": -1}
        )
