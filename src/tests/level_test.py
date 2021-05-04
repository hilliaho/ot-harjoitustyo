import unittest

from services.level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()
        self.level.new_tetromino(name="L")
        self.tetromino = self.level.tetromino

    def test_tetromino_can_move(self):
        self.move_tetromino("left", 1)
        self.assertEqual(self.tetromino.rect.x, 75)

    def test_tetromino_cant_move_through_walls(self):
        self.move_tetromino("left", 5)
        self.assertEqual(self.tetromino.rect.x, 0)

    def test_tetromino_can_rotate(self):
        self.level.rotate_tetromino()
        self.assertEqual(self.tetromino.angle, 270)
    
    def test_tetromino_cant_rotate_through_walls(self):
        self.level.rotate_tetromino()
        self.move_tetromino("left", 5)
        self.level.rotate_tetromino()
        self.assertEqual(self.tetromino.angle, 270)

    def test_full_rows_get_deleted(self):
        self.move_tetromino("down", 25)
        self.level.new_tetromino(name="T")
        self.tetromino = self.level.tetromino
        self.move_tetromino("right", 3)
        self.move_tetromino("down", 25)
        self.level.new_tetromino(name="I")
        self.tetromino = self.level.tetromino
        self.move_tetromino("left", 3)
        self.move_tetromino("down", 25)
        self.level.delete_full_rows()
        self.level.new_tetromino(name="I")
        self.move_tetromino("left", 3)
        self.move_tetromino("down", 25)
        self.assertEqual(self.tetromino.rect.y, 475)
    
    def move_tetromino(self, direction, number):
        for i in range(number):
            self.level.move_tetromino(direction)





