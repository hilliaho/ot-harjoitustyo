import unittest
import pygame

from services.level import Level
from ui.game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level()
        self.level.new_tetromino()

    def test_game_over_works(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE)
        ]

        game_loop = GameLoop(
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        game_loop.start()

        self.assertTrue(self.level.game_over)
        