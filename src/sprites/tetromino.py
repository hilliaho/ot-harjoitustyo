import pygame
import random
from load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, x=100, y=-25, speed=500, name="random"):
        super().__init__()
        self.speed = speed
        self.angle = 0
        self.previous_move_time = 0
        self.name = name
        if self.name == "random":
            self.name = self.random_tetromino()
        filename = self.name + ".png"
        self.image = load_image(filename)
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def random_tetromino(self):
        tetromino_names = "IOTJLSZ"
        i = random.randint(0, 6)
        return tetromino_names[i]

    def rotate(self, clockwise):
        if clockwise == False:
            if self.angle == 270:
                self.angle = 0
            else:
                self.angle += 90
        else:
            if self.angle == 0:
                self.angle = 270
            else:
                self.angle -= 90

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)

    def set_previous_move_time(self, current_time):
        self.previous_move_time = current_time

    def should_move(self, current_time):
        return current_time - self.previous_move_time >= self.speed
