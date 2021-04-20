import pygame
from load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, x=50, y=0, speed=500):
        super().__init__()
        self.speed = speed
        self.previous_move_time = 0

        self.image = load_image("square.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_previous_move_time(self, current_time):
        self.previous_move_time = current_time

    def should_move(self, current_time):
        return current_time - self.previous_move_time >= self.speed