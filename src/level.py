import pygame
from tetromino import Tetromino
from floor import Floor
from wall import Wall

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.tetrominos = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.tetrominos.add(Tetromino(normalized_x, normalized_y))


        self.all_sprites.add(
            self.floors,
            self.walls,
	        self.tetrominos
        )