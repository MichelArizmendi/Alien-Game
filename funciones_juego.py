import sys
from time import sleep
import pygame
from proyectil import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens):
    """Responde a pulsaciones de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Crea una nueva bala y la añade al grupo de balas
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_q:
        if not stats.game_active:
            start_game(ai_settings, screen, ship, aliens, bullets, stats)

def start_game(ai_settings, screen, ship, aliens, bullets, stats):
    """Inicia el juego reiniciando estadísticas y creando una nueva flota."""
    stats.reset_stats()
    stats.game_active = True

    # Vacía las listas de aliens y balas
    aliens.empty()
    bullets.empty()

    # Crea una nueva flota y centra la nave
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Oculta el cursor del ratón durante el juego
    pygame.mouse.set_visible(False)

def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """Responde a key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Responde a eventos de teclado y de ratón, incluyendo el botón de 'Play'."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia un nuevo juego cuando el jugador presiona el botón de play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Restablece la configuración del juego
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active = True

        # Vacía la lista de aliens y balas
        aliens.empty()
        bullets.empty()

        # Crea una nueva flota y centra la nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Oculta el cursor del ratón
        pygame.mouse.set_visible(False)

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Actualiza la posición de las balas y elimina las que han desaparecido."""
    bullets.update()  # Llama al método update de cada bala en el grupo
    # Eliminar balas que han desaparecido de la pantalla
    for bullet in bullets.copy():
        if bullet.rect.left >= bullet.screen.get_width():
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisiones entre balas y aliens."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens_group in collisions.values():
            stats.score += ai_settings.aliens_points * len(aliens_group)  # Cambiado de alien_points a aliens_points
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Elimina las balas restantes y crea una nueva flota de aliens
        bullets.empty()
        ai_settings.increase_speed()  # Aumenta la velocidad al pasar de nivel
        create_fleet(ai_settings, screen, ship, aliens)


def check_aliens_left(ai_settings, stats, screen, ship, aliens, bullets):
    """Comprueba si algún alien ha alcanzado el borde izquierdo de la pantalla."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left <= screen_rect.left:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            ai_settings.increase_speed()  # Aumenta la velocidad al acercarse al borde
            break

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Actualiza las imágenes en la pantalla y alterna al nuevo marco."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # Esto ahora dibuja la estrella junto con la nave
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Dibuja la información sobre puntaje y nivel
    sb.show_score()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


    # Dibuja la información sobre puntaje y nivel
    sb.show_score()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def get_number_aliens(ai_settings, alien_width):
    """Determina el número de aliens que caben en una fila."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = min(4, int(available_space_x / (2 * alien_width)))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina el número de filas de aliens que caben en la pantalla."""
    available_space_y = ai_settings.screen_height - ship_height - 2 * alien_height
    number_rows = int(available_space_y / (2 * alien_height))
    return min(number_rows, 6)  # Limita el número de filas a 6

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Crea un alien y lo coloca en la fila y columna especificada."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # Posiciona el alien en la fila especificada
    alien.x = ai_settings.screen_width - (alien_width + 2 * alien_width * alien_number)
    alien.rect.x = alien.x - alien.rect.width

    alien.rect.y = alien_height + 3 * alien_height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Crea una flota completa de aliens comenzando desde el lado derecho de la pantalla."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    number_aliens_x = get_number_aliens(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien_height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responde a la nave golpeada por un alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Actualiza la posición de los aliens y verifica colisiones."""
    for alien in aliens.sprites():
        alien.update()
        if alien.rect.right < 0:  # Si un alien sale por el lado izquierdo, resetea la posición
            alien.rect.left = alien.screen.get_width()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    
    check_aliens_left(ai_settings, stats, screen, ship, aliens, bullets)

def check_high_score(stats, sb):
    """Comprueba si hay un nuevo puntaje más alto."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()