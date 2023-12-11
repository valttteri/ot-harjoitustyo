import unittest
from unittest.mock import Mock
import pygame
from tests.stubs import (
    StubRenderer,
    StubLevelHandler,
    StubEvent,
    StubClock,
    StubPygameEvents,
    StubUserEvents,
    StubDatabaseHandler,
)
from loop import Loop
from gamestate import GameStateHandler


class TestLoop(unittest.TestCase):
    def setUp(self):
        self.game_state_handler_mock = Mock(
            wraps=GameStateHandler(
                [],
                "level_one",
                StubRenderer("level_one"),
                StubLevelHandler("level_one", 30),
                StubDatabaseHandler()
            )
        )
        self.events = []
        self.loop = Loop(
            "start",
            "level_one",
            StubPygameEvents(self.events),
            self.game_state_handler_mock,
            StubClock(60),
            StubUserEvents(),
        )

    def test_starting_game(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))

        self.loop.start_keys_pressed(self.events[-1])

        self.assertEqual(self.loop.state, "game_on")

    def test_access_high_scores_from_start_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_2))

        self.loop.start_keys_pressed(self.events[-1])

        self.assertEqual(self.loop.state, "high_score")

    def test_quit(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE))
        self.loop.keys_pressed()

        self.assertFalse(self.loop.running)

        self.events.append(StubEvent(pygame.QUIT, pygame.K_1))
        self.loop.running = True
        self.loop.keys_pressed()

        self.assertFalse(self.loop.running)

    def test_close_pause_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_p))

        self.loop.pause_keys_pressed(self.events[-1])

        self.assertEqual(self.loop.state, "game_on")

    def test_start_new_game_from_game_over_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))
        self.loop.running = True

        self.loop.game_over_keys_pressed(self.events[-1])
        self.assertEqual(self.loop.state, "game_on")

    def test_pressing_keys_in_game_over_menu(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))
        self.loop.game_over_keys_pressed(self.events[-1])

        self.assertEqual(self.loop.state, "game_on")

        self.loop.state = "game_over"
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_2))
        self.loop.game_over_keys_pressed(self.events[-1])

        self.assertEqual(self.loop.state, "start")

    def test_correct_execute_state_parameter(self):
        self.loop.execute(True)
        self.game_state_handler_mock.execute_state.assert_called_with("start")

    def test_correct_action_when_new_state(self):
        states = ["pause", "game_over", "victory", "game_on", "high_score"]

        for state in states:
            self.game_state_handler_mock.change_state.return_value = state
            self.loop.execute(True)
            self.assertEqual(self.loop.state, state)
            self.game_state_handler_mock.reset_state.assert_called()

    def test_pressing_game_keys(self):
        events = {
            "up": StubEvent(pygame.KEYDOWN, pygame.K_UP),
            "down": StubEvent(pygame.KEYDOWN, pygame.K_DOWN),
            "left": StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            "right": StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
        }

        for key, value in events.items():
            self.events.append(value)
            self.loop.game_keys_pressed(self.events[-1])
            self.game_state_handler_mock.snake_direction_change.assert_called_with(key)
            self.events.pop()

        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_p))
        self.loop.game_keys_pressed(self.events[-1])
        self.assertEqual(self.loop.state, "pause")

    def test_pressing_keys_at_high_score_screen(self):
        self.events.append(StubEvent(pygame.KEYDOWN, pygame.K_1))
        self.loop.high_score_keys_pressed(self.events[-1])
        self.assertEqual(self.loop.state, "start")
