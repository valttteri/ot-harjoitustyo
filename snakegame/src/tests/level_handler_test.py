import unittest
from unittest.mock import Mock
from levelhandler import LevelHandler
from stubs import StubImageLoader


class TestLevelHandler(unittest.TestCase):
    def setUp(self):
        self.level_handler = LevelHandler("test", 30, StubImageLoader())

    def test_sprite_generation(self):
        self.level_handler.get_sprites()
        self.assertEqual(len(self.level_handler.walls.sprites()), 36)
        self.assertEqual(len(self.level_handler.food.sprites()), 5)
        self.assertEqual(len(self.level_handler.grass.sprites()), 100)
        self.assertIsNotNone(self.level_handler.snake)
