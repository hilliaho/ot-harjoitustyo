import pygame
from load_image import load_image


class Wall(pygame.sprite.Sprite):
    """Luokka, joka kuvaa pelikentän seinän yhtä ruutua.

    Attributes:
        x_coordinate: Ruudun x-koordinaatti.
        y_coordinate: Ruudun y-koordinaatti.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """Luokan konstruktori, joka luo uuden seinäruudun.

        Args:
            x_coordinate: Ruudun x-koordinaatti.
            y_coordinate: Ruudun y-koordinaatti.
        """
        super().__init__()
        self.image = load_image("wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
