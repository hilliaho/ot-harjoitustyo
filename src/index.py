import pygame
import os

pygame.init()
display = pygame.display.set_mode((300, 500))
pygame.display.set_caption("Tetris")

dirname = os.path.dirname(__file__)
tetromino = pygame.image.load(
            os.path.join(dirname, "assets", "square.png")
        )

x = 0
y = 0
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0,0,0))
    display.blit(tetromino, (x, y))
    pygame.display.flip()

    y += 1
    clock.tick(60)
