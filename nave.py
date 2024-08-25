import pygame
import random
from random import randint  # Asegúrate de importar randint

class Ship():
    def __init__(self, ai_settings, screen):
        # Inicializa la nave y establece su posición inicial
        self.screen = screen
        self.ai_settings = ai_settings

        # Carga la imagen de la nave y obtiene su rectángulo
        self.image = pygame.image.load('images/nave.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nueva nave en la parte inferior central de la pantalla
        self.rect.centery = self.screen_rect.centery
        self.rect.midleft = self.screen_rect.midleft

        # Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Carga la imagen de las estrellas y crea una lista de estrellas
        self.star_image = pygame.image.load('images/estrella.png')
        self.stars = pygame.sprite.Group()
        self.create_stars()

    def create_stars(self):
        """Crea 100 estrellas en posiciones aleatorias"""
        for _ in range(100):
            x = randint(0, self.screen_rect.width - self.star_image.get_width())
            y = randint(0, self.screen_rect.height - self.star_image.get_height())
            star = pygame.sprite.Sprite()
            star.image = self.star_image
            star.rect = star.image.get_rect()
            star.rect.x = x
            star.rect.y = y
            self.stars.add(star)

    def update(self):
        """Actualiza la posición de la nave basada en la bandera de movimiento."""
        if self.moving_right and self.rect.right < (self.screen_rect.right)/3:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor

    def blitme(self):
        # Dibuja la nave en su posición actual
        self.screen.blit(self.image, self.rect)
        # Dibuja las estrellas en la pantalla
        for star in self.stars:
            self.screen.blit(star.image, star.rect)

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.center = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.midleft = self.screen_rect.midleft
