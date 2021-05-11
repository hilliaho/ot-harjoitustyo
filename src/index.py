import pygame
from services.game_loop import GameLoop
from services.level import Level
from services.event_queue import EventQueue
from services.clock import Clock
from ui.renderer import Renderer


def main():
    height = 22
    width = 18
    display_height = height * 25
    display_width = width * 25
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Tetris")

    level = Level()
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
