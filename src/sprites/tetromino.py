import random
import pygame
from ui.load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    """Luokka, joka kuvaa yhtä tetromino-palikkaa

    Attributes:
        name: Tetrominon nimi.
        x_coordinate: Tetrominon x-koordinaatti.
        y_coordinate: Tetrominon y-koordinaatti.
    """

    def __init__(self, name, x_coordinate=100, y_coordinate=0):
        """Luokan konstruktori, joka luo uuden tetrominon.

        Args:
            x_coordinate: Vapaaehtoinen, oletusarvo 100. Tetrominon x-koordinaatti.
            y_coordinate: Vapaaehtoinen, oletusarvo 0. Tetrominon y-koordinaatti.
            name: Tetrominon nimi.
        """
        super().__init__()
        self.speed = 0
        self._angle = 0
        self.previous_move_times = [0, 0, 0]
        self.name = name
        if self.name is None:
            self.name = self._random_tetromino()
        if (self.name == "I" or self.name == "O") and x_coordinate == 300:
            x_coordinate += 12
        self.image = load_image(self.name + ".png")
        self._original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.mask = pygame.mask.from_surface(self.image)

    def _random_tetromino(self):
        """Arpoo tetrominolle satunnaisen nimen.

        Returns:
            Arvottu nimi yksittäisenä merkkinä.
        """

        tetromino_names = "IOTJLSZ"
        i = random.randint(0, 6)
        return tetromino_names[i]

    def rotate(self, clockwise):
        """Kääntää tetrominoa 90 astetta joko myötä- tai vastapäivään.

        Tetrominoilla "I", "S" ja "Z" on vain kaksi mahdollista asentoa.
        Muilla tetrominoilla on neljä mahdollista asentoa.

        Args:
            clockwise: Boolean-arvo, joka kertoo, onko kiertosuunta myötäpäivään.
        """
        if self.name == "I" or self.name == "S" or self.name == "Z":
            if self._angle == 0:
                self._angle = 270
            elif self._angle == 270:
                self._angle = 0
        else:
            if clockwise is True:
                if self._angle == 0:
                    self._angle = 270
                else:
                    self._angle -= 90
            else:
                if self._angle == 270:
                    self._angle = 0
                else:
                    self._angle += 90
        self.image = pygame.transform.rotate(self._original_image, self._angle)
        self.mask = pygame.mask.from_surface(self.image)

    def should_move(self, current_time=0, direction="down"):
        """Selvittää, pitääkö tetrominon liikkua.

        Args:
            current_time: Aika tällä hetkellä.

        Returns:
            Boolean-arvo, joka kertoo, onko tetrominon aika liikkua.
        """

        _should_move = False
        if direction == "down":
            _should_move = current_time - \
                self.previous_move_times[0] >= self.speed
        elif direction == "left":
            _should_move = current_time - self.previous_move_times[1] >= 120
        elif direction == "right":
            _should_move = current_time - self.previous_move_times[2] >= 120
        return _should_move
