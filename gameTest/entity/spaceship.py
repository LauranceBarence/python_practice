import pygame
from gameTest.entity.bullet import Bullet
from pygame.sprite import Group


class SpaceShip:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.bottom = float(self.rect.bottom)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 1
        self.bullets = Group()

    def blitme(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.move_left()
        elif self.moving_right:
            self.move_right()
        if self.moving_up:
            self.move_up()
        elif self.moving_down:
            self.move_down()
        self.update_bullets()

    def move_left(self):
        if self.rect.centerx > self.rect.width / 2:
            self.center -= self.speed
            self.rect.centerx = self.center

    def move_right(self):
        if self.rect.centerx < self.screen_rect.width - self.rect.width / 2:
            self.center += self.speed
            self.rect.centerx = self.center

    def move_up(self):
        if self.rect.top > 0:
            self.bottom -= self.speed
            self.rect.bottom = self.bottom

    def move_down(self):
        if self.rect.bottom < self.screen_rect.height:
            self.bottom += self.speed
            self.rect.bottom = self.bottom

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if not bullet.out:
                pass
            else:
                self.bullets.remove(bullet)

    def shoot(self, setting):
        new_bullet = Bullet(setting, self.screen, self)
        self.bullets.add(new_bullet)
