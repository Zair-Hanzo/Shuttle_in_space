import pygame

class Rectangle:
    def __init__(self, sis):
        self.screen = sis.screen
        self.screen_rect = sis.screen.get_rect()
        self.settings = sis.settings
        self.width, self.height = (150, 75) 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # self.rect.topright = self.screen_rect.topright
        self.rect.x, self.rect.y = (self.settings.screen_width - self.width - 10), self.height - 25
        self.rect_color = (60, 120, 240)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def _check_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self):
        self.y += (self.settings.rects_speed * 
                   self.settings.rects_direction)
        self.rect.y = self.y

    def draw_rectangle(self):
        self.screen.fill(self.rect_color, self.rect)

    