import random
import pygame
from load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    """Luokka, joka kuvaa yhtä tetromino-palikkaa

    Attributes:
        x_coordinate: Tetrominon x-koordinaatti.
        y_coordinate: Tetrominon y-koordinaatti.
        name: Tetrominon nimi.
    """

    def __init__(self, name, x_coordinate=100, y_coordinate=0):
        """Luokan konstruktori, joka luo uuden tetrominon.

        Args:
            x_coordinate: Vapaaehtoinen, oletusarvo 100. Tetrominon x-koordinaatti.
            y_coordinate: Vapaaehtoinen, oletusarvo 0. Tetrominon y-koordinaatti.
            name: Tetrominon nimi.
        """
        super().__init__()
        self.speed = 500
        self.angle = 0
        self.previous_move_time = 0
        self.name = name
        if self.name is None:
            self.name = self.random_tetromino()
        if (self.name == "I" or self.name == "O") and x_coordinate == 300:
            x_coordinate += 12
        self.image = load_image(self.name + ".png")
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
        self.mask = pygame.mask.from_surface(self.image)

    def random_tetromino(self):
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
            if self.angle == 0:
                self.angle = 270
            elif self.angle == 270:
                self.angle = 0
        else:
            if clockwise is True:
                if self.angle == 0:
                    self.angle = 270
                else:
                    self.angle -= 90
            else:
                if self.angle == 270:
                    self.angle = 0
                else:
                    self.angle += 90
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)

    def set_previous_move_time(self, current_time):
        """Pitää kirjaa siitä, milloin tetromino on liikkunut viimeksi.

        Args:
            current_time: Aika tällä hetkellä.
        """
        self.previous_move_time = current_time

    def should_move(self, current_time):
        """Selvittää, pitääkö tetrominon liikkua.

        Args:
            current_time: Aika tällä hetkellä.

        Returns:
            Boolean-arvo, joka kertoo, onko tetrominon aika liikkua.
        """
        return current_time - self.previous_move_time >= self.speed
