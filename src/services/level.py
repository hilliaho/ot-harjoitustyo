import pygame
from sprites.tetromino import Tetromino
from sprites.background import Background
from sprites.wall import Wall
from sprites.text import Text


class Level:
    """Luokka, joka vastaa pelikentän tilan hallinnasta."""

    def __init__(self):
        """Luokan konstruktori, joka luo uuden pelikentän tilasta vastaavan palvelun"""

        self._score = Text(0, 300, 225, 30)
        self._level = Text(1, 300, 300, 30)
        self.start_game_button = Text("START GAME", 300, 375, 25, (255, 0, 0))
        self._tetromino = None
        self._next_tetromino = Tetromino(None, 300, 40)
        self.direction = None
        self._tetrominoes = pygame.sprite.Group()
        self._backgrounds = pygame.sprite.Group()
        self._obstacles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def update(self, current_time, dropped):
        """Päivittää pelikentän tilan.

        Selvittää, mitä pelikentällä kuuluu tapahtua seuraavaksi,
        ja kutsuu tarvittavia metodeja.

        Args:
            current_time: Aika tällä hetkellä.
        """

        if self._game_over() is False:
            if self._tetromino is None:
                self._new_tetromino()

            if dropped or self._tetromino.should_move(current_time, "down"):
                if not self._tetromino_can_move("down"):
                    self._deactivate_tetromino()
                    self._delete_full_rows()
                    self._level_up()
                    self._new_tetromino()
                else:
                    self._move_ip("down")
                self._tetromino.previous_move_times[0] = current_time

            if self.direction == "left" and self._tetromino.should_move(current_time, "left"):
                self._move_tetromino("left")
                self._tetromino.previous_move_times[1] = current_time

            elif self.direction == "right" and self._tetromino.should_move(current_time, "right"):
                self._move_tetromino("right")
                self._tetromino.previous_move_times[2] = current_time

    def _new_tetromino(self, name=None):
        """Luo uuden tetrominon ja lisää sen kaikkien spritejen ryhmään.

        Args:
            name: Vapaaehtoinen, oletusarvo None. Tetrominon nimi.
        """

        if name is None:
            name = self._next_tetromino.name
        self._tetromino = Tetromino(name)
        self.all_sprites.add(self._tetromino)
        self._next_tetromino.kill()
        self._next_tetromino = Tetromino(None, 300, 40)
        self.all_sprites.add(self._next_tetromino)
        self.set_tetromino_speed(1)

    def _game_over(self):
        """Selvittää, onko pelin aika päättyä.

        Returns:
            Boolean-arvo, joka kertoo, lopetetaanko peli.
        """

        if self._tetromino is None:
            return False
        if self._tetromino.rect.y == 0 and not self._tetromino_can_move("down"):
            self.all_sprites.add(Text("GAME", 300, 350, 52, (255, 0, 0)))
            self.all_sprites.add(Text("OVER", 300, 400, 52, (255, 0, 0)))
            return True
        return False

    def _level_up(self):
        """korottaa tasoa tarvittaessa"""

        level_content = self._level.content
        if self._score.content >= 5*level_content**2:
            level_content += 1
            self._level.kill()
            self._level = Text(level_content,
                               300, 300,  30)
            self.all_sprites.add(self._level)

    def _move_tetromino(self, direction):
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
            self._tetromino.rect.move_ip(-25, 0)
        elif direction == "right":
            self._tetromino.rect.move_ip(25, 0)
        elif direction == "down":
            self._tetromino.rect.move_ip(0, 25)
        elif direction == "up":
            self._tetromino.rect.move_ip(0, -25)

    def rotate_tetromino(self, clockwise=True):
        """Kiertää tetrominoa haluttuun suuntaan.

        Args:
            clockwise: Vapaaehtoinen, oletusarvo True.
            Boolean-arvo, joka kertoo onko kiertosuunta myötäpäivään.
        """

        self._tetromino.rotate(clockwise)
        if self._collide(self._tetromino, self._obstacles):
            self._tetromino.rotate(not clockwise)

    def drop_tetromino(self):
        """pudottaa tetrominon"""

        while self._tetromino_can_move("down"):
            self._move_ip("down")

    def _deactivate_tetromino(self):
        """Deaktivoi maahan pudonneen tetrominon."""

        colliding = self._collide(self._tetromino, self._backgrounds)
        for background in colliding:
            tetromino = Tetromino(self._tetromino.name + "_color",
                                  background.rect.x, background.rect.y)
            self.all_sprites.add(tetromino)
            self._obstacles.add(tetromino)
            self._tetrominoes.add(tetromino)
        self._tetromino.kill()

    def _detect_full_rows(self):
        """Selvittää, mitkä rivit ovat täynnä.

        Returns:
            Lista kaikista täysistä riveistä.
        """

        full_rows = list(range(1, 21))
        for background in self._backgrounds:
            if not self._collide(background, self._tetrominoes):
                row = background.rect.y/25
                if row in full_rows:
                    full_rows.remove(row)
        return full_rows

    def _delete_full_rows(self):
        """Poistaa täynnä olevat rivit."""

        full_rows = self._detect_full_rows()
        for tetromino in self._tetrominoes:
            row = tetromino.rect.y/25
            if row in full_rows:
                tetromino.kill()
        self._score.content += len(full_rows)**2
        score_content = self._score.content
        self._score.kill()
        self._score = Text(score_content,
                           300, 225, 30)
        self.all_sprites.add(self._score)
        self._drop_remaining_rows(full_rows)

    def _drop_remaining_rows(self, empty_rows):
        """Pudottaa jäljellä olevia rivejä alaspäin."""

        for row in empty_rows:
            for tetromino in self._tetrominoes:
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
        if self._collide(self._tetromino, self._obstacles):
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

    def set_tetromino_speed(self, speed):
        """Muuttaa tetrominon nopeutta.

        Args:
            speed: Tetrominon nopeus.
        """
        if speed == 1:
            self._tetromino.speed = 600 - self._level.content*50
        elif speed == 2:
            self._tetromino.speed = 50

    def _initialize_sprites(self):
        """Alustaa pelikentän tausta-, seinä- ja teksti-spritet."""

        height = 22
        width = 18

        for row in range(height):
            for col in range(width):
                x_coordinate = col * 25
                y_coordinate = row * 25
                if (0 < row < 21 and 0 < col < 11) or (0 < row < 6 and 11 < col < 17):
                    self._backgrounds.add(Background(
                        x_coordinate, y_coordinate))
                else:
                    self._obstacles.add(Wall(x_coordinate, y_coordinate))

        score_text = Text("score", 300, 200, 30)
        level_text = Text("level", 300, 275, 30)

        self.all_sprites.add(
            self._backgrounds,
            self._obstacles,
            self._score,
            self._level,
            self.start_game_button,
            score_text,
            level_text
        )
