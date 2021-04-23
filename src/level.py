import pygame
from tetromino import Tetromino
from background import Background
from wall import Wall
from floor import Floor


class Level:
    def __init__(self, level_map, cell_size, speed):
        self.count = 0
        self.cell_size = cell_size
        self.tetromino = None
        self.tetrominos = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.level_map = level_map
        self._initialize_sprites()
        self.previous_new_tetromino_time = 0
        self.speed = speed

    def update(self, current_time):
        if self.count == 0:
            print("count: ", str(self.count))
            self.new_tetromino()

        if self.tetromino.should_move(current_time):
            self.move_tetromino(dy=25)
            self.tetromino.set_previous_move_time(current_time)

    def new_tetromino(self):
        if not self.tetromino == None:
            self.tetrominos.add(self.tetromino)
        self.tetromino = Tetromino(
            x=len(self.level_map[0])*self.cell_size//2, speed=self.speed)
        self.all_sprites.add(self.tetromino)
        self.count += 1
        print("count: ", str(self.count))

    def move_tetromino(self, dx=0, dy=0):
        self.tetromino.rect.move_ip(dx, dy)
        if pygame.sprite.spritecollide(self.tetromino, self.floors, False):
            self.tetromino.rect.move_ip(-dx, -dy)
            self.new_tetromino()
        if self.tetromino.rect.y > 25 and pygame.sprite.spritecollide(self.tetromino, self.walls, False):
            self.tetromino.rect.move_ip(-dx, -dy)
        if pygame.sprite.spritecollide(self.tetromino, self.tetrominos, False, pygame.sprite.collide_mask):
            self.tetromino.rect.move_ip(-dx, -dy)
            self.new_tetromino()

    def drop_tetromino(self):
        self.tetromino.speed = 0

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

        self.all_sprites.add(
            self.backgrounds,
            self.walls,
            self.floors
        )
