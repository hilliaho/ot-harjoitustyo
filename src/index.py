import pygame
from level import Level
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

LEVEL_MAP_2 = [[1, 1, 1, 1, 1, 1],
               [1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1]]

CELL_SIZE = 25

SPEED = 300


def main():
    level_map = LEVEL_MAP
    height = len(level_map)
    width = len(level_map[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Tetris")

    level = Level(level_map, CELL_SIZE, SPEED)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
