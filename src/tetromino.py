import pygame
from load_image import load_image


class Tetromino(pygame.sprite.Sprite):
    def __init__(self, x=50, y=0, speed=500):
        super().__init__()
        self.speed = speed
        self.angle = 0
        self.previous_move_time = 0

        self.image = load_image("L_1.png")
        self.original_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self):
        print("rotate now")
        if self.angle == 270:
            self.angle = 0
        else:
            self.angle += 90
        
        self.image = pygame.transform.rotate(self.original_image, self.angle)


    def set_previous_move_time(self, current_time):
        self.previous_move_time = current_time

    def should_move(self, current_time):
        return current_time - self.previous_move_time >= self.speed
