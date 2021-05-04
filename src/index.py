import pygame
from services.level import Level
from ui.game_loop import GameLoop
from services.event_queue import EventQueue
from services.renderer import Renderer
from services.clock import Clock


def main():
    height = 22
    width = 12
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
