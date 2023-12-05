import unittest
import pygame
from loop import Loop


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubPygameEvents:
    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events


class StubGameEventHandler:
    def __init__(self, level):
        self.level = level

    def reset_score(self):
        print("score was reset")

    def save_final_score(self):
        print("score was submitted")


class StubRenderer:
    def __init__(self):
        pass


class StubClock:
    def __init__(self, fps):
        self.fps = fps


class StubUserEvents:
    def __init__(self):
        self.nothing = 1


class TestLoop(unittest.TestCase):
    def setUp(self):
        self.events = []
        self.loop = Loop(
            "start",
            "level_one",
            StubPygameEvents(self.events),
            StubGameEventHandler("level_one"),
            StubClock(60),
            StubUserEvents(),
        )

    def test_starting_game(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))

        self.loop.start_keys_pressed()

        self.assertEqual(self.loop.state, "game_on")

    def test_access_high_scores_from_start_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_2))

        self.loop.start_keys_pressed()

        self.assertEqual(self.loop.state, "high_score")

    def test_quit_game_from_start_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE))
        self.loop.start_keys_pressed()

        self.assertFalse(self.loop.running)

        self.events.append(StubEvent(pygame.QUIT, pygame.K_1))
        self.loop.running = True
        self.loop.start_keys_pressed()

        self.assertFalse(self.loop.running)

        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_3))
        self.loop.running = True
        self.loop.start_keys_pressed()

        self.assertFalse(self.loop.running)

    def test_close_pause_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_p))

        self.loop.pause_keys_pressed()

        self.assertEqual(self.loop.state, "game_on")

    def test_quit_game_from_pause_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE))
        self.loop.pause_keys_pressed()

        self.assertFalse(self.loop.running)

        self.events.append(StubEvent(pygame.QUIT, pygame.K_1))
        self.loop.running = True

        self.loop.pause_keys_pressed()
        self.assertFalse(self.loop.running)

    def test_quit_game_from_game_over_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE))
        self.loop.game_over_keys_pressed()

        self.assertFalse(self.loop.running)

        self.events.append(StubEvent(pygame.QUIT, pygame.K_1))
        self.loop.running = True

        self.loop.game_over_keys_pressed()
        self.assertFalse(self.loop.running)

    def test_start_new_game_from_game_over_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))
        self.loop.running = True

        self.loop.game_over_keys_pressed()
        self.assertEqual(self.loop.state, "game_on")

    def test_pressing_keys_in_game_over_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))
        self.loop.game_over_keys_pressed()

        self.assertEqual(self.loop.state, "game_on")

        self.loop.state = "game_over"
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_2))
        self.loop.game_over_keys_pressed()

        self.assertEqual(self.loop.state, "start")

        self.loop.state = "game_over"
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_3))
        self.loop.game_over_keys_pressed()

        self.assertEqual(self.loop.state, "start")
