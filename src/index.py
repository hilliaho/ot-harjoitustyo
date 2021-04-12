import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

naytto.fill((0,0,0))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()