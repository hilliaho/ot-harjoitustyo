import pygame
from level import Level
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

LEVEL_MAP = [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 2, 2, 2, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

CELL_SIZE = 50

def main():
    height = len(LEVEL_MAP)
    width = len(LEVEL_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Sokoban")

    level = Level(LEVEL_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
