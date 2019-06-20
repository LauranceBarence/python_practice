import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.top)
        self.color = setting.bullet_color
        self.speed = setting.bullet_speed
        self.out = False

    def update(self, direct=1):
        if self.rect.y > -self.rect.height:
            self.y -= self.speed*direct
            self.rect.y = self.y
        else:
            self.out = True

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
