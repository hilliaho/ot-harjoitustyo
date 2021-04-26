import pygame
from sprites.tetromino import Tetromino
from sprites.background import Background
from sprites.wall import Wall


class Level:
    def __init__(self, level_map):
        self.score = 0
        self.tetromino = None
        self.tetrominoes = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)

    def update(self, current_time):
        if self.score == 0:
            self._new_tetromino()

        if self.tetromino.should_move(current_time):
            if not self._tetromino_can_move("down"):
                if self.game_over() is True:
                    return
                self._deactivate_tetromino()
                self._delete_full_rows()
                self._new_tetromino()
            else:
                self._move_tetromino("down")
            self.tetromino.set_previous_move_time(current_time)

    def _deactivate_tetromino(self):
        colliding = self._collide(self.tetromino, self.backgrounds)
        for background in colliding:
            tetromino = Tetromino(
                background.rect.x, background.rect.y, 0, self.tetromino.name + "_color")
            self.all_sprites.add(tetromino)
            self.obstacles.add(tetromino)
            self.tetrominoes.add(tetromino)
        self.tetromino.kill()

    def _detect_full_rows(self):
        full_rows = list(range(1, 21))
        for background in self.backgrounds:
            if not self._collide(background, self.tetrominoes):
                row = background.rect.y/25
                if row in full_rows:
                    full_rows.remove(row)
        return full_rows

    def _delete_full_rows(self):
        full_rows = self._detect_full_rows()
        for tetromino in self.tetrominoes:
            row = tetromino.rect.y/25
            if row in full_rows:
                tetromino.kill()
        empty_rows = full_rows
        self._drop_remaining_rows(empty_rows)

    def _drop_remaining_rows(self, empty_rows):
        for row in empty_rows:
            for tetromino in self.tetrominoes:
                if tetromino.rect.y/25 < row:
                    tetromino.rect.y += 25

    def _new_tetromino(self):
        self.tetromino = Tetromino()
        self.all_sprites.add(self.tetromino)
        self.score += 1

    def game_over(self):
        if self.tetromino is None:
            return False
        if self.tetromino.rect.y == 0 and not self._tetromino_can_move("down"):
            print("score:", str(self.score))
            return True
        return False

    def move_tetromino_if_possible(self, direction):
        if self._tetromino_can_move(direction) is True:
            self._move_tetromino(direction)

    def _move_tetromino(self, direction):
        if direction == "left":
            self.tetromino.rect.move_ip(-25, 0)
        elif direction == "right":
            self.tetromino.rect.move_ip(25, 0)
        elif direction == "down":
            self.tetromino.rect.move_ip(0, 25)
        elif direction == "up":
            self.tetromino.rect.move_ip(0, -25)

    def rotate_tetromino(self, clockwise):
        self.tetromino.rotate(clockwise)
        if self._collide(self.tetromino, self.obstacles):
            self.tetromino.rotate(not clockwise)

    def set_tetromino_speed(self, speed):
        self.tetromino.speed = speed

    def _tetromino_can_move(self, direction):
        can_move = True
        self._move_tetromino(direction)
        if self._collide(self.tetromino, self.obstacles):
            can_move = False
        opposite_direction = self._opposite_direction(direction)
        self._move_tetromino(opposite_direction)
        return can_move

    def _collide(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )

    def _opposite_direction(self, direction):
        if direction == "left":
            opposite_direction = "right"
        elif direction == "right":
            opposite_direction = "left"
        elif direction == "down":
            opposite_direction = "up"
        return opposite_direction

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for row in range(height):
            for col in range(width):
                cell = level_map[row][col]
                x_coordinate = col * 25
                y_coordinate = row * 25

                if cell == 0:
                    self.backgrounds.add(Background(
                        x_coordinate, y_coordinate))
                elif cell == 1:
                    self.obstacles.add(Wall(x_coordinate, y_coordinate))

        self.all_sprites.add(
            self.backgrounds,
            self.obstacles
        )
