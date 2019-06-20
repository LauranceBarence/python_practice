import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from gameTest.entity.bullet import Bullet


class Alien(Sprite):
    def __init__(self, screen, setting, x):
        super().__init__()
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load('./assets/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width if (x - self.rect.width) > 0 else self.rect.width
        self.rect.y = 0 - self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.out = False
        self.speed = setting.enemy_speed
        self.direct = 1
        self.lock = False
        self.bullets = Group()

    def update(self):
        self.moving()
        self.update_bullets()
        if self.lock:
            self.shooting()

    def moving(self):
        self.y += self.speed
        self.rect.y = self.y
        self.x += (self.speed * self.direct)
        self.rect.x = self.x
        if self.rect.y < self.screen.get_rect().height / 2:
            if self.rect.x > 0 and self.rect.x < (self.screen.get_rect().width - self.rect.width):
                pass
            else:
                self.direct *= -1
        elif self.rect.y > self.screen.get_rect().height:
            self.out = True
        else:
            if self.rect.x < 0 or self.rect.x > self.screen.get_rect().width:
                self.out = True

    def shooting(self):
        new_bullet = Bullet(self.setting, self.screen, self)
        self.bullets.add(new_bullet)

    def blitme(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.screen.blit(self.image, self.rect)

    def update_bullets(self):
        self.bullets.update(-1)
        for bullet in self.bullets.sprites():
            if not bullet.out:
                pass
            else:
                self.bullets.remove(bullet)
