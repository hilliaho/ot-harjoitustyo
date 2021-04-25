import pygame
from tetromino import Tetromino
from background import Background
from wall import Wall
from floor import Floor
from fake_wall import FakeWall
from ground_tetromino import GroundTetromino


class Level:
    def __init__(self, level_map, cell_size, speed):
        self.score = 0
        self.cell_size = cell_size
        self.tetromino = None
        self.tetrominos = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.fake_walls = pygame.sprite.Group()
        self.ground_tetrominos = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.Group()
        self.level_map = level_map
        self._initialize_sprites()
        self.previous_new_tetromino_time = 0
        self.speed = speed
        self.game_over = False

    def update(self, current_time):
        if self.score == 0:
            self.new_tetromino()

        if self.tetromino.should_move(current_time):
            self.move_tetromino(dy=25)
            self.tetromino.set_previous_move_time(current_time)

    def new_tetromino(self):
        if not self.tetromino == None:
            colliding=pygame.sprite.spritecollide(self.tetromino, self.backgrounds, False, pygame.sprite.collide_mask)
            for background in colliding:
                ground_tetromino = GroundTetromino(color=self.tetromino.color, x=background.rect.x, y=background.rect.y)
                self.all_sprites.add(ground_tetromino)
                self.all_obstacles.add(ground_tetromino)
                self.ground_tetrominos.add(ground_tetromino)
            self.tetromino.kill()
            full_rows=list(range(1,21))
            for background in self.backgrounds:
                if not pygame.sprite.spritecollide(background, self.ground_tetrominos, False, pygame.sprite.collide_mask):
                    row = background.rect.y/25
                    if row in full_rows:
                        full_rows.remove(row)
            for ground_tetromino in self.ground_tetrominos:
                row = ground_tetromino.rect.y/25
                if row in full_rows:
                    ground_tetromino.kill()
            for row in full_rows:
                for ground_tetromino in self.ground_tetrominos:
                    if ground_tetromino.rect.y/25 < row:
                        ground_tetromino.rect.y += 25
                        
                

        self.tetromino = Tetromino(speed=self.speed)
        self.all_sprites.add(self.tetromino)
        self.score += 1

    def move_tetromino(self, dx=0, dy=0):
        if not self.can_move(dx, dy):
            if dy == 25:
                if self.tetromino.rect.y < 25:
                    print("score:", str(self.score))
                    self.game_over = True
                self.new_tetromino()
            return
        self.tetromino.rect.move_ip(dx, dy)

    def rotate_tetromino(self, clockwise):
        self.tetromino.rotate(clockwise)
        if pygame.sprite.spritecollide(self.tetromino, self.all_obstacles, False, pygame.sprite.collide_mask):
            self.tetromino.rotate(not clockwise)

    def set_tetromino_speed(self, speed):
        self.tetromino.speed = speed

    def can_move(self, dx=0, dy=0):
        can_move=True
        self.tetromino.rect.move_ip(dx, dy)
        if pygame.sprite.spritecollide(self.tetromino, self.all_obstacles, False, pygame.sprite.collide_mask):
            can_move=False
        self.tetromino.rect.move_ip(-dx, -dy)
        return can_move

    def _initialize_sprites(self):
        height = len(self.level_map)
        width = len(self.level_map[0])

        for y in range(height):
            for x in range(width):
                cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.backgrounds.add(Background(
                        normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 3:
                    self.fake_walls.add(FakeWall(normalized_x, normalized_y))

        self.all_sprites.add(
            self.backgrounds,
            self.walls,
            self.floors,
            self.fake_walls
        )

        self.all_obstacles.add(
            self.walls,
            self.floors
        )
