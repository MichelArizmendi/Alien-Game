import sys
import pygame
from pygame.sprite import Group

import funciones_juego as gf
from configuracion import Settings
from st_game import GameStats
from score import Scoreboard 
from boton import Button
from nave import Ship
from alien import Alien

def run_game():
    # Inicializa el juego y crea un objeto para la pantalla
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasión Alienígena")

    # Crea el botón de play
    play_button = Button(ai_settings, screen, "Jugar o presiona 'Q'")

    # Crea una instancia para almacenar estadísticas del juego
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Crea una nave
    ship = Ship(ai_settings, screen)

    # Crea un grupo en el que se almacenarán los proyectiles
    bullets = Group()
    aliens = Group()


    # Crea una flota alien
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # Inicia el bucle principal del juego
    while True:
        gf.check_events(ai_settings, screen,stats, play_button, ship, aliens, bullets)
        if stats.game_active: # Si el juego está activo, debera correr esto:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats,sb, ship, aliens, bullets)  # Actualiza la posición de los proyectiles
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)  

        gf.update_screen(ai_settings, screen,stats, sb, ship, aliens,bullets, play_button)

run_game()
