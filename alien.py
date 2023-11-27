import pygame
from pygame.sprite import Sprite
# from settings import Settings

class Alien(Sprite):
    def __init__(self, al):
        super().__init__()
        self.screen = al.screen
        self.screen_rect = al.screen.get_rect()
        self.settings = al.settings

        self.image = pygame.image.load("images/alien1.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

    def check_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        self.y += (self.settings.alien_speed * 
                   self.settings.aliens_direction)
        self.rect.y = self.y

