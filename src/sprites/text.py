import pygame
import pygame.freetype

pygame.init()


class Text(pygame.sprite.Sprite):
    """Luokka, joka kuvaa yhtä riviä tekstiä.

    Attributes:
        x_coordinate: Tekstin x-koordinaatti.
        y_coordinate: Tekstin y-koordinaatti.
    """

    def __init__(self, content, x_coordinate, y_coordinate, font_size, background_color=(0, 0, 0)):
        """Luokan konstruktori, joka luo uuden tekstin.

        Args:
            content: Tekstin sisältö.
            x_coordinate: Tekstin x-koordinaatti.
            y_coordinate: Tekstin y-koordinaatti.
            font_size: Tekstin koko.
            background_color: Taustan väri.
        """
        super().__init__()
        self.content = content
        self.image = pygame.Surface((120, font_size))
        self.image.fill(background_color)
        self.image.blit(pygame.font.SysFont(None, font_size).render(
            str(content), True, (255, 255, 255)), [5, 4])
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate
