import sys
import pygame


def check_events(settings, ship):
    for event in pygame.event.get():
        check_exit(event)
        check_key_down_events(event, settings, ship)
        check_key_up_events(event, ship)


def check_exit(event):
    if event.type == pygame.QUIT:
        sys.exit()


def check_key_down_events(event, settings, ship):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE or event.key == pygame.K_k:
            if len(ship.bullets) < settings.max_bullet:
                ship.shoot(settings)


def check_key_up_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            ship.moving_down = False
        elif event.key == pygame.K_ESCAPE:
            sys.exit()


def update_screen(setting, screen, ship, alien_factory):
    screen.fill(setting.bg_color)
    ship.blitme()
    for alien in alien_factory.aliens.sprites():
        alien.blitme()
    pygame.display.flip()
