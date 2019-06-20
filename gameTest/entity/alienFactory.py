from pygame.sprite import Group
from gameTest.entity.alien import Alien
import random


class AlienFactory:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.aliens = Group()

    def update(self, ship):
        self.aliens.update()
        for alien in self.aliens.sprites():
            if alien.out:
                self.destroy_alien(alien)
            else:
                if alien.rect.centerx == ship.rect.centerx:
                    alien.lock = True
                else:
                    alien.lock = False
        if len(self.aliens) < self.settings.max_enemy:
            self.create_alien()

    def create_alien(self):
        x = random.randint(0, self.screen_rect.width)
        # while True:
        #     x = random.randint(0, self.screen_rect.width)
        #     has_one = False
        #     for alien in self.aliens.sprites():
        #         if x < (alien.rect.x - (alien.rect.width*2)) or x > (alien.rect.x + (alien.rect.width*2)):
        #             continue
        #         else:
        #             has_one = True
        #             break
        #     if not has_one:
        #         pass
        #         break
        new_alien = Alien(self.screen, self.settings, x)
        new_alien.direct = random.sample([1, -1], 1)[0]
        self.aliens.add(new_alien)

    def destroy_alien(self, alien):
        self.aliens.remove(alien)
