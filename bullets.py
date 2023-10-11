import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, agame):
        super().__init__()
        self.screen = agame.screen
        self.settings = agame.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = agame.shuttle.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        