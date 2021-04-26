import pygame
from load_image import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__()

        self.image = load_image("background.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
