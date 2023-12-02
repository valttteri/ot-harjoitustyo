import unittest
import pygame
from loop import Loop
pygame.init()

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubPygameEvents:
    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events

class TestLoop(unittest.TestCase):
    def test_starting_game(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_1)
        ]

        loop = Loop("start", StubPygameEvents(events))
        loop.start_keys_pressed()

        self.assertEqual(loop.state, "game_on")
    
    def test_quit_game_from_start_menu(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE)
        ]

        loop = Loop("start", StubPygameEvents(events))
        loop.start_keys_pressed()

        self.assertFalse(loop.running)

    def test_close_pause_menu(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_p)
        ]

        loop = Loop("pause", StubPygameEvents(events))
        loop.pause_keys_pressed()

        self.assertEqual(loop.state, "game_on")

    def test_quite_game_from_pause_menu(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE)
        ]

        loop = Loop("pause", StubPygameEvents(events))
        loop.pause_keys_pressed()

        self.assertFalse(loop.running)
