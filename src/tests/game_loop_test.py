import unittest
import pygame
from services.level import Level
from services.game_loop import GameLoop
from services.clock import Clock

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

    def test_can_drop_tetromino(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE),
        ]

        game_loop = GameLoop(
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            Clock()
        )

        game_loop.start()

        self.assertTrue(self.level.tetromino.rect.y > 400)
