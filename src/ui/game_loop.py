import pygame


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            if self._level.game_over() is True:
                break

            current_time = self._clock.get_ticks()

            self._level.update(current_time)
            self._render()
            self._clock.tick(100)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_tetromino("left")
                if event.key == pygame.K_RIGHT:
                    self._level.move_tetromino("right")
                if event.key == pygame.K_UP:
                    self._level.rotate_tetromino()
                if event.key == pygame.K_DOWN:
                    self._level.tetromino.speed=50
                if event.key == pygame.K_SPACE:
                    self._level.tetromino.speed=0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self._level.tetromino.speed=500
            elif event.type == pygame.QUIT:
                return False
        return True

    def _render(self):
        self._renderer.render()
