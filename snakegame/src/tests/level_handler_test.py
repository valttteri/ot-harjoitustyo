import unittest
from levelhandler import LevelHandler
from tests.stubs import StubImageLoader
from objects.score import Score


class TestLevelHandler(unittest.TestCase):
    def setUp(self):
        self.level_handler = LevelHandler("test", 30, StubImageLoader(), Score(0))
        self.level_handler.get_sprites()

    def test_sprite_generation(self):
        self.assertEqual(len(self.level_handler.walls.sprites()), 36)
        self.assertEqual(len(self.level_handler.food.sprites()), 5)
        self.assertEqual(len(self.level_handler.grass.sprites()), 100)
        self.assertIsNotNone(self.level_handler.snake)

    def test_interacting_with_score(self):
        self.level_handler.increase_score()
        self.level_handler.increase_score()
        self.assertEqual(self.level_handler.level_score(), 2)

        self.level_handler.reset_level_score()
        self.assertEqual(self.level_handler.level_score(), 0)

    def test_victory(self):
        self.level_handler.increase_score()
        self.assertFalse(self.level_handler.victory())

        for _ in range(100):
            self.level_handler.increase_score()
        self.level_handler.victory()

        self.assertTrue(self.level_handler.victory())

    def test_snake_collision(self):
        self.level_handler.snake_move()
        self.assertFalse(self.level_handler.snake_collision())

        self.level_handler.snake_move()
        self.level_handler.snake_move()
        self.level_handler.snake_move()
        self.assertTrue(self.level_handler.snake_collision())
