import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase para representar un solo alien en la flota."""

    def __init__(self, ai_settings, screen):
        """Inicializa el alien y establece su posición inicial."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carga la imagen del alien y establece su atributo rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Posiciona el alien en la esquina superior derecha de la pantalla
        self.rect.topright = (self.screen.get_width(), 0)

        # Almacena la posición exacta del alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja el alien en su posición actual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Mueve el alien a la izquierda."""
        self.x -= self.ai_settings.alien_speed_factor
        self.rect.x = self.x

