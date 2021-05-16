import pygame


class GameLoop:
    """Luokka, joka vastaa pelisilmukan pyörittämisestä."""

    def __init__(self, level, renderer, event_queue, clock):
        """Luokan konstruktori, joka luo uuden gameloopin.

        Args:
            level: Pelikentän tilasta vastaava palvelu.
            renderer: Näkymän piirtämisestä vastaava palvelu.
            event_queue: Tapahtumajonosta vastaava palvelu.
            clock: Ajastuksesta vastaava palvelu.
        """

        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._running = False

    def start(self):
        """Pyörittää peliä silmukan avulla"""

        while True:
            if self._handle_events() is False:
                break
            self._render()
            if self._running:
                self._level.update(self._clock.get_ticks(), False)
                self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if self._running is False:
                self._handle_events_before_game(event)
            else:
                self._handle_events_during_game(event)
        return True

    def _handle_events_before_game(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self._level.start_game_button.kill()
                self._running = True
        if self._level.start_game_button.rect.collidepoint(pygame.mouse.get_pos()):
            self._level.start_game_button.update((200, 0, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._level.start_game_button.kill()
                self._running = True
        else:
            self._level.start_game_button.update((255, 0, 0))

    def _handle_events_during_game(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._level.direction = "left"
            if event.key == pygame.K_RIGHT:
                self._level.direction = "right"
            if event.key == pygame.K_UP:
                self._level.rotate_tetromino()
            if event.key == pygame.K_DOWN:
                self._level.set_tetromino_speed(2)
            if event.key == pygame.K_SPACE:
                self._level.drop_tetromino()
                self._level.update(self._clock.get_ticks(), True)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self._level.set_tetromino_speed(1)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self._level.direction = None

    def _render(self):
        self._renderer.render()
