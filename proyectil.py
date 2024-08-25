import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase que administra proyectiles disparados por la nave"""

    def __init__(self, ai_settings, screen, ship):
        """Crea un objeto para el proyectil en la posición actual de la nave."""
        super().__init__()
        self.screen = screen

        # Crea un rectpángulo para el proyectil en (0, 0) y luego establece la posición correcta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right  # Coloca el proyectil al borde derecho de la nave

        # Almacena la posición del proyectil como un valor decimal
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Mueve el proyectil hacia adelante en la pantalla (a la derecha)."""
        # Actualiza la posición decimal del proyectil
        self.x += self.speed_factor
        # Actualiza la posición del rectángulo
        self.rect.x = self.x

    def draw_bullet(self):
        """Dibuja el proyectil en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)
