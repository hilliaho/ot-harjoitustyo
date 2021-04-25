import pygame
from load_image import load_image


class GroundTetromino(pygame.sprite.Sprite):
    def __init__(self, color, x=0, y=0):
        super().__init__()

        self.image = load_image(color + "_color.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
