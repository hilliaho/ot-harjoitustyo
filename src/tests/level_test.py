import unittest

from services.level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()

    def test_tetromino_can_move(self):
        self.level._new_tetromino(name="I")
        self.move_tetromino("left", 1)
        self.assertEqual(self.level._tetromino.rect.x, 75)

    def test_tetromino_cant_move_through_walls(self):
        self.level._new_tetromino(name="I")
        self.move_tetromino("left", 5)
        self.assertEqual(self.level._tetromino.rect.x, 25)

    def test_tetromino_can_rotate(self):
        self.level._new_tetromino(name="I")
        self.move_tetromino("down", 2)
        self.level.rotate_tetromino()
        self.assertEqual(self.level._tetromino._angle, 270)

    def test_tetromino_angle_is_zero_after_rotating_four_times(self):
        self.level._new_tetromino(name="L")
        self.move_tetromino("down", 2)
        self.level.rotate_tetromino()
        self.level.rotate_tetromino()
        self.level.rotate_tetromino()
        self.level.rotate_tetromino()
        self.assertEqual(self.level._tetromino._angle, 0)

    def test_tetromino_angle_is_zero_after_rotating_two_times(self):
        self.level._new_tetromino(name="S")
        self.move_tetromino("down", 2)
        self.level.rotate_tetromino()
        self.level.rotate_tetromino()
        self.assertEqual(self.level._tetromino._angle, 0)

    def test_tetromino_cant_rotate_through_walls(self):
        self.level._new_tetromino(name="L")
        self.move_tetromino("down", 2)
        self.level.rotate_tetromino()
        self.move_tetromino("left", 5)
        self.level.rotate_tetromino()
        self.assertEqual(self.level._tetromino._angle, 270)

    def test_tetromino_cant_move_through_tetromino(self):
        self.fill_rows(2)
        self.level._new_tetromino(name="O")
        self.level.drop_tetromino()
        self.assertEqual(self.level._tetromino.rect.y, 400)

    def test_full_rows_get_deleted(self):
        self.fill_rows(2)
        self.level._delete_full_rows()
        self.level._new_tetromino(name="I")
        self.level.drop_tetromino()
        self.assertEqual(self.level._tetromino.rect.y, 475)

    def test_level_up(self):
        self.fill_rows(4)
        self.level._delete_full_rows()
        self.level._level_up()
        self.assertEqual(self.level._level.content, 2)

    def test_score(self):
        self.fill_rows(4)
        self.level._delete_full_rows()
        self.assertEqual(self.level._score.content, 16)

    def test_level_update(self):
        self.level._new_tetromino(name="T")
        self.level.update(0, True)
        self.assertEqual(self.level._tetromino.rect.y, 25)

    def test_game_over(self):
        self.drop_tetromino(18)
        self.level._new_tetromino(name="O")
        self.level.drop_tetromino()
        self.assertEqual(self.level._game_over(), True)

    def test_update_deletes_full_rows(self):
        self.fill_rows(10)
        self.level._new_tetromino(name="S")
        self.level.drop_tetromino()
        self.level.update(0, True)
        self.level.drop_tetromino()
        self.assertTrue(self.level._tetromino.rect.y >= 400)

    def test_update_increases_level(self):
        self.fill_rows(4)
        self.level._new_tetromino(name="J")
        self.level.drop_tetromino()
        self.level.update(0, True)
        self.assertEqual(self.level._level.content, 2)

    def test_level_update_creates_new_tetromino(self):
        self.level.update(0, True)
        self.assertNotEqual(self.level._tetromino, None)

    def move_tetromino(self, direction, number):
        for i in range(number):
            self.level._move_tetromino(direction)

    def fill_rows(self, number):
        list = ["left", 4, "left", 2, "left", 0, "right", 2, "right", 4]
        i = 0
        while i < number:
            j = 0
            while j < len(list):
                self.level._new_tetromino(name="O")
                self.move_tetromino(list[j], list[j+1])
                self.level.drop_tetromino()
                self.level._deactivate_tetromino()
                j += 2
            i += 2

    def drop_tetromino(self, number):
        i = 0
        while i < number:
            self.level._new_tetromino(name="O")
            self.level.drop_tetromino()
            self.level._deactivate_tetromino()
            i += 1
