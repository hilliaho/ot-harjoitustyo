import unittest

from level import Level

LEVEL_MAP =   [[1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1]]

CELL_SIZE = 25
SPEED = 100

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)

    def test_tetromino_can_move(self):
        tetromino = self.level.tetromino(SPEED)

        self.assertEqual(tetromino.rect.x, len(LEVEL_MAP[0])*CELL_SIZE//2)

        self.level.move_tetromino(dx=CELL_SIZE)
        self.assertEqual(tetromino.rect.x, len(LEVEL_MAP[0])*CELL_SIZE//2-CELL_SIZE)
