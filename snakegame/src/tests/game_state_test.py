import unittest
from gamestate import GameStateHandler
from tests.stubs import StubDatabaseHandler, StubRenderer, StubLevelHandler


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
