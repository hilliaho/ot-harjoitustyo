import pygame
import random
from load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, x=100, y=-25, speed=500):
        super().__init__()
        self.speed = speed
        self.angle = 0
        self.previous_move_time = 0
        self.tetromino_names = "IOTJLSZ"
        self.color = None
        self.image = self.random_tetromino()
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        
    def random_tetromino(self):
        i = random.randint(0, 6)
        filename = self.tetromino_names[i] + ".png"
        self.color = self.tetromino_names[i]
        tetromino_image = load_image(filename)
        return tetromino_image

    def rotate(self, cw):
        if cw == False:
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
