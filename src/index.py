import pygame

pygame.init()
pygame.display.set_caption("Tetris")
display = pygame.display.set_mode((300, 500))

display.fill((0,0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()