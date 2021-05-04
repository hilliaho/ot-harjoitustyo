import pygame
from sprites.tetromino import Tetromino
from sprites.background import Background
from sprites.wall import Wall


class Level:
    """Luokka, joka vastaa pelikentän tilan hallinnasta."""

    def __init__(self):
        """Luokan konstruktori, joka luo uuden pelikentän tilasta vastaavan palvelun"""

        self.score = 0
        self.tetromino = None
        self.tetrominoes = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def update(self, current_time):
        """Päivittää pelikentän tilan.

        Selvittää, mitä pelikentällä kuuluu tapahtua seuraavaksi,
        ja kutsuu tarvittavia metodeja.

        Args:
            current_time: Aika tällä hetkellä.
        """

        if self.score == 0:
            self.score += 1
            self.new_tetromino()

        if self.tetromino.should_move(current_time):
            if not self._tetromino_can_move("down"):
                if self.game_over() is True:
                    return
                self._deactivate_tetromino()
                self.delete_full_rows()
                self.score += 1
                self.new_tetromino()
            else:
                self._move_ip("down")
            self.tetromino.set_previous_move_time(current_time)

    def new_tetromino(self, name=None):
        """Luo uuden tetrominon ja lisää sen kaikkien spritejen ryhmään.

        Args:
            name: Vapaaehtoinen, oletusarvo None. Tetrominon nimi.
        """

        self.tetromino = Tetromino(name)
        self.all_sprites.add(self.tetromino)

    def game_over(self):
        """Selvittää, onko pelin aika päättyä.

        Returns:
            Boolean-arvo, joka kertoo, lopetetaanko peli.
        """

        if self.tetromino is None:
            return False
        if self.tetromino.rect.y == 0 and not self._tetromino_can_move("down"):
            print("score:", str(self.score))
            return True
        return False

    def move_tetromino(self, direction):
        """Liikuttaa tetrominoa haluttuun suuntaan, jos se on mahdollista.

        Args:
            direction: Tetrominon liikkumissuunta.
        """

        if self._tetromino_can_move(direction) is True:
            self._move_ip(direction)

    def _move_ip(self, direction):
        """Siirtää tetrominon haluttuun paikkaan.

        Args:
            direction: Tetrominon siirtämissuunta.
        """

        if direction == "left":
            self.tetromino.rect.move_ip(-25, 0)
        elif direction == "right":
            self.tetromino.rect.move_ip(25, 0)
        elif direction == "down":
            self.tetromino.rect.move_ip(0, 25)
        elif direction == "up":
            self.tetromino.rect.move_ip(0, -25)

    def rotate_tetromino(self, clockwise=True):
        """Kiertää tetrominoa haluttuun suuntaan.

        Args:
            clockwise: Vapaaehtoinen, oletusarvo True.
            Boolean-arvo, joka kertoo onko kiertosuunta myötäpäivään.
        """

        self.tetromino.rotate(clockwise)
        if self._collide(self.tetromino, self.obstacles):
            self.tetromino.rotate(not clockwise)

    def _deactivate_tetromino(self):
        """Deaktivoi maahan pudonneen tetrominon."""

        colliding = self._collide(self.tetromino, self.backgrounds)
        for background in colliding:
            tetromino = Tetromino(self.tetromino.name + "_color",
                                  background.rect.x, background.rect.y)
            self.all_sprites.add(tetromino)
            self.obstacles.add(tetromino)
            self.tetrominoes.add(tetromino)
        self.tetromino.kill()

    def _detect_full_rows(self):
        """Selvittää, mitkä rivit ovat täynnä.

        Returns:
            Lista kaikista täysistä riveistä.
        """

        full_rows = list(range(1, 21))
        for background in self.backgrounds:
            if not self._collide(background, self.tetrominoes):
                row = background.rect.y/25
                if row in full_rows:
                    full_rows.remove(row)
        return full_rows

    def delete_full_rows(self):
        """Poistaa täynnä olevat rivit."""

        full_rows = self._detect_full_rows()
        for tetromino in self.tetrominoes:
            row = tetromino.rect.y/25
            if row in full_rows:
                tetromino.kill()
        empty_rows = full_rows
        self._drop_remaining_rows(empty_rows)

    def _drop_remaining_rows(self, empty_rows):
        """Pudottaa jäljellä olevia rivejä alaspäin."""

        for row in empty_rows:
            for tetromino in self.tetrominoes:
                if tetromino.rect.y/25 < row:
                    tetromino.rect.y += 25

    def _tetromino_can_move(self, direction):
        """Selvittää, voiko tetromino liikkua haluttuun suuntaan.

        Args:
            direction: Tetrominon liikkumissuunta.

        Returns:
            Boolean-arvo, joka kertoo voiko tetromino liikkua.
        """
        can_move = True
        self._move_ip(direction)
        if self._collide(self.tetromino, self.obstacles):
            can_move = False
        opposite_direction = self._opposite_direction(direction)
        self._move_ip(opposite_direction)
        return can_move

    def _collide(self, sprite, group):
        """Selvittää, törmäävätkö spritet toisiinsa.

        Args:
            sprite: Sprite, jonka törmäämistä tarkastellaan.
            group: Ryhmä spritejä, joiden törmäämistä tarkastellaan.

        Returns:
            Ryhmä, joka sisältää kaikki ryhmän spritet, 
            jotka törmäävät tarkastellun spriten kanssa.
        """
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask
        )

    def _opposite_direction(self, direction):
        """Määrittää halutulle suunnalle vastakkaisen suunnan.

        Args:
            direction: Alkuperäinen suunta merkkijonona.

        Returns:
            Vastakkainen suunta merkkijonona.
        """
        if direction == "left":
            opposite_direction = "right"
        elif direction == "right":
            opposite_direction = "left"
        elif direction == "down":
            opposite_direction = "up"
        return opposite_direction

    def _initialize_sprites(self):
        """Alustaa pelikentän tausta- ja seinä-spritet"""

        height = 22
        width = 12

        for row in range(height):
            for col in range(width):
                if row == 0 or row == 21 or col == 0 or col == 11:
                    cell = 1
                else:
                    cell = 0
                x_coordinate = col * 25
                y_coordinate = row * 25

                if cell == 0:
                    self.backgrounds.add(Background(
                        x_coordinate, y_coordinate))
                elif cell == 1:
                    self.obstacles.add(Wall(x_coordinate, y_coordinate))

        self.all_sprites.add(
            self.backgrounds,
            self.obstacles
        )
