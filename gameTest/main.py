from gameTest.entity.settings import Settings
from gameTest.entity.spaceship import SpaceShip
from gameTest.game_functions import *
from gameTest.entity.alienFactory import AlienFactory


def run():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption('Alien shooter')
    ship = SpaceShip(screen)
    ship.speed = setting.ship_speed
    alien_factory = AlienFactory(screen, setting)
    while True:
        check_events(setting, ship)
        ship.update()
        alien_factory.update(ship)
        update_screen(setting, screen, ship, alien_factory)


def main():
    run()


if __name__ == '__main__':
    main()
