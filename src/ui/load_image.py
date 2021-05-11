import os
import pygame


def load_image(filename):
    return pygame.image.load(
        os.path.join("src", "assets", filename)
    )
