import unittest
from unittest.mock import Mock
from levelhandler import LevelHandler
from stubs import StubImageLoader
from score import Score


class TestLevelHandler(unittest.TestCase):
    def setUp(self):
        self.level_handler_mock = Mock(wraps=LevelHandler("test", 30, StubImageLoader(), Score(0)))
        self.level_handler_mock.get_sprites()

    def test_sprite_generation(self):
        self.assertEqual(len(self.level_handler_mock.walls.sprites()), 36)
        self.assertEqual(len(self.level_handler_mock.food.sprites()), 5)
        self.assertEqual(len(self.level_handler_mock.grass.sprites()), 100)
        self.assertIsNotNone(self.level_handler_mock.snake)

    def test_interacting_with_score(self):
        self.level_handler_mock.increase_score()
        self.level_handler_mock.increase_score()
        self.assertEqual(self.level_handler_mock.level_score(), 2)

        self.level_handler_mock.reset_level_score()
        self.assertEqual(self.level_handler_mock.level_score(), 0)
    
    def test_victory(self):
        self.level_handler_mock.increase_score()
        self.assertFalse(self.level_handler_mock.victory())

        for i in range(100):
            self.level_handler_mock.increase_score()
        self.level_handler_mock.victory()

        self.assertTrue(self.level_handler_mock.victory())

    def test_snake_collision(self):
        self.level_handler_mock.snake_move()
        self.assertFalse(self.level_handler_mock.snake_collision())

        self.level_handler_mock.snake_move()
        self.level_handler_mock.snake_move()
        self.level_handler_mock.snake_move()
        self.assertTrue(self.level_handler_mock.snake_collision())
